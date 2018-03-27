import json
import logging as logger
import os
import sys
from odmservices import ServiceManager

logger.basicConfig(level=logger.DEBUG)

src_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
root_directory = os.path.realpath(os.path.join(src_directory, os.pardir, os.pardir))
static_folder = os.path.join(root_directory, 'static', 'mdfserver', 'json')
sys.path.insert(0, src_directory)

service_manager = ServiceManager()

site_variables = {
    "climate": ['BP_Avg', 'RH', 'VaporPress_Avg', 'WindSp_Avg',
                'WindDir_Avg', 'JuddDepth_Avg', 'PARIn_Avg', 'PAROut_Avg',
                'SWOut_NR01_Avg', 'SWIn_NR01_Avg', 'NetRad_NR01_Avg', 'LWOut_Cor_NR01_Avg', 'LWIn_Cor_NR01_Avg',
                'Evapotrans_ETo', 'Evapotrans_ETr', 'VWC_5cm_Avg', 'SoilTemp_5cm_Avg', 'Permittivity_5cm_Avg',
                'VWC_10cm_Avg', 'SoilTemp_10cm_Avg', 'Permittivity_10cm_Avg', 'VWC_20cm_Avg', 'SoilTemp_20cm_Avg',
                'Permittivity_20cm_Avg', 'VWC_50cm_Avg', 'SoilTemp_50cm_Avg', 'Permittivity_50cm_Avg',
                'VWC_100cm_Avg', 'SoilTemp_100cm_Avg', 'Permittivity_100cm_Avg'],
    "aquatic": ['WaterTemp_EXO', 'SpCond', 'pH', 'ODO', 'ODO_Local', 'TurbMed', 'BGA',
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
        variables.append('AirTemp_ST110_Avg')
        if database == 'iUTAH_Provo_OD':
            variables.insert(0, 'AirTemp_Avg')
            variables.insert(7, 'Rain_Tot')
        else:
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

    service_manager._current_connection = {
        'engine': os.getenv('IUTAH_DB_ENGINE'),
        'user': os.getenv('IUTAH_DB_USER'),
        'password': os.getenv('IUTAH_DB_PASSWORD'),
        'address': os.getenv('IUTAH_DB_ADDRESS'),
        'port': os.getenv('IUTAH_DB_PORT'),
        'db': watershed_database
    }

    # service_manager._current_connection = {
    #     'engine': 'mysql',
    #     'user': 'root',
    #     'password': 'password',
    #     'address': 'localhost',
    #     'port': 1443,
    #     'db': watershed_database
    # }

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
    if sys.platform != 'win32':
        path = os.path.join(os.getcwd(), os.pardir, 'mdfserver', 'static', 'mdfserver', 'json', '%sSite.json' % watershed_name)
        path = os.path.realpath(path)
    else:
        path = os.path.join('%s', '%sSite.json') % (static_folder, watershed_name)
    with open(path, "w") as out_file:
        json.dump(watershed_dictionary, out_file, indent=4)


def initialize_database():
    """
    Run this method for first time setup of database. Creates database(s) based on the models in the odmdata folder.

    For some reason, which we may never know, you need to add connection information in a file named
    'connection.config', located in a directory determined by 'odmservices.utilities.util.resource_path()'.

    To add a database connection info, add a line in 'connection.config' in the format of:
        <engine> <user_name> <password> <address> <database_name>

    Example of 'connection.config' with three connections:
    ================================================
    mysql root password localhost iUTAH_Logan_OD
    mysql root password localhost iUTAH_RedButte_OD
    mssql admin_1 soopersekretpaswurd database.somewhere.else.com iUTAH_Provo_OD
    ================================================

    Yup, pretty genius.

    My sincerest hope is this project will burn to the ground before anyone else might find this comment useful.
    """
    for conn in service_manager.get_connections():
        if service_manager.database_exists(conn_dict=conn):
            continue

        try:
            service_manager.create_database(conn_dict=conn)

            try:
                service_manager.create_tables(conn_dict=conn)
            except Exception:
                raise Exception("Failed to create tables for database '{0}'".format(conn['db']))

        except Exception:
            raise Exception("Failed to create database '{0}'".format(conn.get('db', 'N/A')))


# initialize_database()

parse_data()

