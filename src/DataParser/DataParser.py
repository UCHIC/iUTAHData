import sys
import os
import shutil
import logging

this_file = os.path.realpath(__file__)
directory = os.path.dirname(os.path.dirname(this_file))

sys.path.insert(0, directory)
from odmservices import ServiceManager
from logger import LoggerTool

tool = LoggerTool()
logger = tool.setupLogger(__name__, __name__ + '.log', 'a', logging.DEBUG)

sm = ServiceManager()
# This variable is to address ocassional 500 errors in the sandbox server.
# I think these errors are due to the files are being generated in the static folder.
temp_location = directory + "\\DataParser\\json_temp\\"
dump_location = os.path.join(directory,  "mdfserver\\static\\mdfserver\\json\\")
parent_dir = os.path.join(os.path.join(directory, os.pardir), os.pardir)
static_folder = os.path.join(parent_dir, "static\\mdfserver\\json\\")
NINETY_SIX = 96
DEFAULT_SITE_VARS = ['BP_Avg', 'RH', 'DewPt_Avg', 'VaporPress_Avg', 'WindSp_Avg', 'WindDir_Avg', 'JuddDepth_Avg',
                     'PARIn_Avg', 'PAROut_Avg', 'SWOut_NR01_Avg', 'SWIn_NR01_Avg', 'NetRad_NR01_Avg',
                     'LWOut_Cor_NR01_Avg','LWIn_Cor_NR01_Avg', 'Evapotrans_ETo', 'Evapotrans_ETr', 'VWC_5cm_Avg',
                     'SoilTemp_5cm_Avg', 'Permittivity_5cm_Avg', 'VWC_10cm_Avg', 'SoilTemp_10cm_Avg',
                     'Permittivity_10cm_Avg', 'VWC_20cm_Avg', 'SoilTemp_20cm_Avg', 'Permittivity_20cm_Avg',
                     'VWC_50cm_Avg', 'SoilTemp_50cm_Avg', 'Permittivity_50cm_Avg', 'VWC_100cm_Avg',
                     'SoilTemp_100cm_Avg', 'Permittivity_100cm_Avg']
STREAM_SITE_VARS = ['WaterTemp_EXO', 'SpCond', 'pH', 'ODO', 'ODO_Sat', 'TurbMed', 'BGA', 'Chlorophyll', 'fDOM', 'Stage']
STORM_SEWER_SITE_VARS = ['Flow', 'Level', 'Velocity', 'Volume', 'WaterTemp_ISCO']


def getSiteVars(site, database):
    if site.code == "LR_Wilkins_R":
        return ['AirTemp_HMP50_Avg', 'RH_HMP51', 'WindSp_S_WVT', 'WindDir_D1_WVT']
    elif site.code == "RB_ARBR_USGS":
        return ['USGSTemp', 'USGSStage', 'USGSDischarge']
    elif site.code != 'PR_TC_CUWCD' and site.code != 'RB_RBR_CUWCD' and site.code[-5:] == 'CUWCD':
        return ['CUWCDDischarge']
    elif site.type == "Stream":
        return STREAM_SITE_VARS
    elif site.type == "Storm sewer":
        return STORM_SEWER_SITE_VARS
    vars_to_show = []
    vars_to_show.extend(DEFAULT_SITE_VARS)
    if database == 'iUTAH_Provo_OD':
        vars_to_show.insert(0, 'AirTemp_Avg')
        vars_to_show.insert(7, 'Rain_Tot')
        if site.code == 'PR_CH_C' or site.code == 'PR_ST_C':
            vars_to_show.insert(8, 'Precip_Tot_Avg')
    else:
        vars_to_show.insert(0, 'AirTemp_ST110_Avg')
        vars_to_show.insert(7, 'Precip_Tot_Avg')

    return vars_to_show


# all the tabs and spaces are added for easier debugging.
# Don't judge... the performance increase for taking them out is not even significant.
def handleConnection(database, text_file):
    sm._current_connection = {'engine': 'mssql', 'user': 'webapplication', 'password': 'W3bAppl1c4t10n!',
                              'address': 'iutahdbs.uwrl.usu.edu', 'db': database}
    ss = sm.get_series_service()
    sites = ss.get_all_sites()

    # lets print all the sites, shall we?
    logger.info("Started getting sites for " + database)
    for site in sites:
        # Print all info for each site here
        file_str = ""
        file_str += "\"" + str(site.code) +"\": {\n"
        file_str += "\t\"info\": {\n"
        file_str += "\t\t\"code\": \"{}\",\n".format(site.code)
        file_str += "\t\t\"name\": \"{}\",\n".format(site.name)
        file_str += "\t\t\"latitude\": \"{}\",\n".format(site.latitude)
        file_str += "\t\t\"longitude\": \"{}\",\n".format(site.longitude)
        file_str += "\t\t\"lat_long_datum\": \"{}\",\n".format(site.spatial_ref.srs_name)
        file_str += "\t\t\"elevation\": \"{}\",\n".format(site.elevation_m)
        file_str += "\t\t\"local_x\": \"{}\",\n".format(site.local_x)
        file_str += "\t\t\"local_y\": \"{}\",\n".format(site.local_y)
        file_str += "\t\t\"local_projection\": \"{}\",\n".format(site.local_spatial_ref.srs_name
                                                                 if site.local_spatial_ref else "None")
        file_str += "\t\t\"pos_accuracy\": \"{}\",\n".format(site.pos_accuracy_m)
        file_str += "\t\t\"state\": \"{}\",\n".format(site.state)
        file_str += "\t\t\"county\": \"{}\",\n".format(site.county)
        file_str += "\t\t\"comments\": \"{}\",\n".format(site.comments)
        file_str += "\t\t\"type\": \"{}\",\n".format(site.type)
        file_str += "\t\t},\n\n"

        #process data update time
        update_time = ss.get_min_and_max_value_dates_by_site_id(site.id)
        file_str += "\t\"update_time\": {\n"
        file_str += "\t\t\"min\": \"{}\",\n".format(update_time[0].local_date_time if update_time[0] else "None")
        file_str += "\t\t\"max\": \"{}\",\n".format(update_time[1].local_date_time if update_time[1] else "None")
        file_str += "\t\t},\n\n"

        #print each variable and its value here, bye
        logger.info("Started getting variables for site: " + site.name + " in " + database)
        file_str += "\t\"vars\": [\n"
        vars_to_show = getSiteVars(site, database)

        log_info = "\n"
        no_vars = True
        variables = ss.get_variables_by_site_code(site.code)
        for var_sel in vars_to_show:
            var_print = next((var for var in variables if var.code == var_sel), None)

            if var_print is not None:
                no_vars = False
                file_str += "\t{\n"
                file_str += "\t\t\"name\": \"{}\",\n".format(var_print.name)
                file_str += "\t\t\"unit\": \"{}\",\n".format(var_print.variable_unit.abbreviation)
                file_str += "\t\t\"code\": \"{}\",\n".format(var_print.code)
                file_str += "\t\t\"sample\": \"{}\",\n".format(var_print.sample_medium)
                file_str += "\t\t\"values\": ["
                log_info += "\t\t   Now getting values for {}\n".format(var_print.name)
                var_values = ss.get_num_of_values_by_site_id_and_var_id(site.id, var_print.id, NINETY_SIX)
                threshold = NINETY_SIX
                if len(var_values) < threshold:
                    threshold = len(var_values)
                for x in range(0, threshold):
                    file_str += str(var_values[x].data_value)
                    if x != (threshold - 1):
                        file_str += ", "
                file_str += "]\n\t},\n"
            else:
                log_info += "\t\t\tVar code \"" + var_sel + "\" not found in site: " + site.code + "\n"
        if not no_vars:
            file_str = file_str[:-2]
            
        logger.info(log_info)
        logger.info("Finished getting variables for site: " + site.name + " in " + database)
        file_str += "\n\t]\n}"
        if sites[len(sites) - 1] != site:
            file_str += ","
        file_str += "\n\n"
        text_file.write(file_str)
    logger.info("Finished getting sites for " + database)
    pass


def dataParser():
    logger.info("\n========================================================\n")
    #logan database is loaded here
    logger.info("Started creating files.")
    databaseParser('iUTAH_Logan_OD', 'Logan')
    #provo database is loaded here
    databaseParser('iUTAH_Provo_OD', 'Provo')
    #red butte creek database is loaded here
    databaseParser('iUTAH_RedButte_OD', 'RedButte')
    logger.info("Finished Program and Provo Site. ")

    logger.info("Started moving JSON files to static folder. ")
    moveToStaticFolders("LoganSite.json")
    moveToStaticFolders("ProvoSite.json")
    moveToStaticFolders("RedButteSite.json")

    logger.info("Finished moving JSON files to static folder. ")
    logger.info("\n========================================================\n")


def moveToStaticFolders(fileSite):
    shutil.copy(temp_location + fileSite, static_folder)
    shutil.copy(temp_location + fileSite, dump_location)


def databaseParser(database, location):
    logger.info("Started " + location + " JSON File.")
    text_file = open(temp_location + location + "Site.json", "w")
    logger.info("Started creating " + location + " JSON file. ")
    #JSON File begins
    text_file.write("{\n")
    handleConnection(database, text_file)
    text_file.write("}")
    text_file.close()
    logger.info("Finished creating " + location + " JSON file. ")

dataParser()
