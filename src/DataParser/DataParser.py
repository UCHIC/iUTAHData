import json
import logging
import os
import shutil
from datetime import datetime
import sys

src_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
root_directory = os.path.realpath(os.path.join(src_directory, os.pardir, os.pardir))
static_folder = os.path.join(root_directory, 'static', 'mdfserver', 'json')
sys.path.insert(0, src_directory)

from odmservices import ServiceManager
from logger import LoggerTool

tool = LoggerTool()
logger = tool.setupLogger(__name__, __name__ + '.log', 'a', logging.DEBUG)

service_manager = ServiceManager()

site_variables = {
    "climate": ['BP_Avg', 'RH', 'DewPt_Avg', 'VaporPress_Avg', 'WindSp_Avg',
                'WindDir_Avg', 'JuddDepth_Avg', 'PARIn_Avg', 'PAROut_Avg',
                'SWOut_NR01_Avg', 'SWIn_NR01_Avg', 'NetRad_NR01_Avg', 'LWOut_Cor_NR01_Avg', 'LWIn_Cor_NR01_Avg',
                'Evapotrans_ETo', 'Evapotrans_ETr', 'VWC_5cm_Avg', 'SoilTemp_5cm_Avg', 'Permittivity_5cm_Avg',
                'VWC_10cm_Avg', 'SoilTemp_10cm_Avg', 'Permittivity_10cm_Avg', 'VWC_20cm_Avg', 'SoilTemp_20cm_Avg',
                'Permittivity_20cm_Avg', 'VWC_50cm_Avg', 'SoilTemp_50cm_Avg', 'Permittivity_50cm_Avg',
                'VWC_100cm_Avg', 'SoilTemp_100cm_Avg', 'Permittivity_100cm_Avg'],
    "aquatic": ['WaterTemp_EXO', 'SpCond', 'pH', 'ODO', 'ODO_Sat', 'TurbMed', 'BGA',
                'Chlorophyll', 'fDOM', 'Stage', 'Nitrate-N'],
    "storm_drain": ['Level_ISCO', 'Velocity_ISCO', 'Flow_ISCO', 'Volume_ISCO', 'WaterTemp_ISCO'],

    "wilkins_repeater": ['AirTemp_HMP50_Avg', 'RH_HMP51', 'WindSp_S_WVT', 'WindDir_D1_WVT'],
    "rb_dent_sd__rb_cr_sd": ['Level_Judd', 'JuddTemp', 'Flow_Manning'],
    "rb_900w_ba": ['Level_ISCO'],
    'rb_ldf_a': ['Discharge_cms']
}

decommissioned_sites = ['RB_KF_R', 'PR_TC_CUWCD', 'RB_RBR_CUWCD']


def get_site_variables(site, database):
    variables = []
    if site.type in ['Land', 'Atmosphere']:
        variables.extend(site_variables['climate'])
        if database == 'iUTAH_Provo_OD':
            variables.insert(0, 'AirTemp_Avg')
            variables.insert(7, 'Rain_Tot')
        else:
            variables.insert(0, 'AirTemp_ST110_Avg')
            variables.insert(7, 'Precip_Tot_Avg')
    elif site.type == 'Stream':
        variables.extend(site_variables['aquatic'])
    elif site.type == 'Storm sewer':
        variables.extend(site_variables['storm_drain'])

    if site.code == 'LR_Wilkins_R':
        variables = site_variables['wilkins_repeater']
    elif site.code in ['RB_Dent_SD', 'RB_CR_SD']:
        variables = site_variables['rb_dent_sd__rb_cr_sd']
    elif site.code == 'RB_LKF_A':
        variables.extend(site_variables['rb_ldf_a'])
    elif site.code == 'RB_900W_BA':
        variables.extend(site_variables['rb_900w_ba'])

    return variables


def load_watershed_data(watershed_database):
    # HEY! LET'S ADD THE FILE CONTAINING THE PRODUCTION DATABASE LOGIN TO A PUBLIC REPOSITORY!
    # TODO: for all that is sacred, remove the database authentication info from here.
    service_manager._current_connection = {
        'engine': 'mssql',
        'user': 'webapplication',
        'password': 'W3bAppl1c4t10n!',
        'address': 'iutahdbs.uwrl.usu.edu',
        'db': watershed_database
    }

    watershed = {}
    logger.info("Getting sites for %s" % watershed_database)
    series_service = service_manager.get_series_service()

    sites = series_service.get_all_sites()
    raw_qc_level_id = series_service.get_raw_qc_level_id()

    for site in sites:
        if site.code in decommissioned_sites:
            logger.info("Skipping site %s" % site.code)
            continue

        logger.info("Getting data for site %s" % site.code)
        last_observation_time = series_service.get_site_last_observation_time(site.id)
        site_series = series_service.get_site_series_by_variable_codes(site.id, raw_qc_level_id,
                                                                       get_site_variables(site, watershed_database))
        data_values = series_service.get_site_variables_raw_values(site.id, raw_qc_level_id,
                                                                   [series.variable_id for series in site_series],
                                                                   last_observation_time)

        site_dict = {
            'info': site.get_site_dict(),
            'last_observation': str(last_observation_time),
            'vars': []
        }

        for series in site_series:
            values = data_values.loc[data_values['VariableID'] == series.variable_id]['DataValue'].tolist()
            if len(values) == 0:
                logger.info("No data points for variable %s" % series.variable_code)
                continue
            logger.info("Collected %s data points for variable %s" % (len(values), series.variable_code))
            site_dict['vars'].append({
                'name': series.variable_name,
                'unit': series.units.abbreviation,
                'code': series.variable_code,
                'sample': series.sample_medium,
                'values': values
            })
        watershed[site.code] = site_dict
        logger.info("Finished site data collection for for %s" % site.code)

    return watershed


def parse_data():
    logger.info("\n========================================================\n")
    logger.info("Creating data files.")

    # logan database is loaded here
    logan_watershed = load_watershed_data('iUTAH_Logan_OD')
    write_json(logan_watershed, 'Logan')

    # provo database is loaded here
    provo_watershed = load_watershed_data('iUTAH_Provo_OD')
    write_json(provo_watershed, 'Provo')

    # red butte creek
    red_butte_watershed = load_watershed_data('iUTAH_RedButte_OD')
    write_json(red_butte_watershed, 'RedButte')

    logger.info("Finished creating data files.")
    logger.info("\n========================================================\n")


def write_json(watershed_dictionary, watershed_name):
    with open(os.path.join('%s', '%sSite.json') % (static_folder, watershed_name), "w") as out_file:
        json.dump(watershed_dictionary, out_file, indent=4)


parse_data()
