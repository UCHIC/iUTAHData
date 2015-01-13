import sys
import os
import pyodbc
import time
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
 #This variable is to address ocassional 500 errors in the sandbox server.
 #I think these errors are because the files are being generated in the static folder.
temp_location = "C:\\json_files\\"

dump_location = "C:\\inetpub\\wwwroot\\mdf\\iUTAHData\\src\\mdfserver\\static\\mdfserver\\json\\"
static_folder = "C:\\inetpub\\wwwroot\\mdf\\static\\mdfserver\\json\\"

#all the tabs and spaces are added for easier debugging. Don't judge... the performance increase for taking them out is not even significant.
def handleConnection(database, text_file):
    sm._current_connection= {'engine':'mssql', 'user':'webapplication' , 'password':'W3bAppl1c4t10n!', 'address':'iutahdbs.uwrl.usu.edu', 'db':database}
    ss = sm.get_series_service()
    sites = ss.get_all_sites()

    #lets print all the sites, shall we?
    file_str = ""
    logger.info("Started getting sites for " + database)
    for site in sites:
        file_str += "\t\t\t\"" + str(site.code) +"\": {\n"
        #Print all info for each site here
        file_str += "\t\t\t\t\"info\": {\n"
        file_str += "\t\t\t\t\t\"code\": \""+ str(site.code) +"\",\n"
        file_str += "\t\t\t\t\t\"name\": \""+str(site.name) +"\",\n"
        file_str += "\t\t\t\t\t\"latitude\": \""+str(site.latitude) +"\",\n"
        file_str += "\t\t\t\t\t\"longitude\": \""+str(site.longitude) +"\",\n"
        file_str += "\t\t\t\t\t\"lat_long_datum\": \""+str(site.spatial_ref.srs_name) +"\",\n" 
        file_str += "\t\t\t\t\t\"elevation\": \""+str(site.elevation_m) +"\",\n"
        file_str += "\t\t\t\t\t\"local_x\": \""+str(site.local_x) +"\",\n"
        file_str += "\t\t\t\t\t\"local_y\": \""+str(site.local_y) +"\",\n"
        file_str += "\t\t\t\t\t\"local_projection\": \"" + (str(site.local_spatial_ref.srs_name) if site.local_spatial_ref else "None" ) +"\",\n" 
        file_str += "\t\t\t\t\t\"pos_accuracy\": \""+str(site.pos_accuracy_m) +"\",\n"
        file_str += "\t\t\t\t\t\"state\": \""+str(site.state) +"\",\n"
        file_str += "\t\t\t\t\t\"county\": \""+str(site.county) +"\",\n"
        file_str += "\t\t\t\t\t\"comments\": \""+str(site.comments) +"\",\n"
        file_str += "\t\t\t\t\t\"type\": \""+str(site.type) +"\"\n"
        file_str += "\t\t\t\t\t},\n\n"

        #process data update time
        updateTime = []
        updateTime = ss.get_min_and_max_value_dates_by_site_id(site.id)
        file_str += "\t\t\t\t\"update_time\": {\n"
        file_str += "\t\t\t\t\t\"min\": \"" + (str(updateTime[0].local_date_time) if updateTime[0] else "None") + "\",\n"
        file_str += "\t\t\t\t\t\"max\": \"" + (str(updateTime[1].local_date_time) if updateTime[1] else "None") + "\"\n"
        file_str += "\t\t\t\t\t},\n\n"
        
        
        #print each variable and its value here, bye
        file_str += "\t\t\t\t\"vars\": [\n"
        variables = ss.get_variables_by_site_code(site.code)
        logger.info("Started getting variables for site: " + site.name + " in " + database)
        loginfo = "\n"
        if site.code == "LR_Wilkins_R":
            vars_to_show = ['AirTemp_HMP50_Avg', 'RH_HMP51', 'WindSp_S_WVT', 'WindDir_D1_WVT']
        elif site.code == "RB_ARBR_USGS":
            vars_to_show = ['USGSTemp', 'USGSStage', 'USGSDischarge']
        elif site.code == "PR_BJ_CUWCD" or site.code == "PR_CH_CUWCD" or site.code == "PR_LM_CUWCD" or site.code == "PR_UM_CUWCD":
            vars_to_show = ['CUWCDDischarge']
        elif site.type == "Stream":
            vars_to_show = ['WaterTemp_EXO', 'SpCond', 'pH', 'ODO', 'ODO_Sat', 'TurbMed', 'BGA', 'Chlorophyll', 'fDOM', 'Stage' ]
        elif site.type == "Storm sewer":
            vars_to_show = ['Flow', 'Level', 'Velocity', 'Volume', 'WaterTemp_ISCO' ]
        else:
            vars_to_show = [
                'BP_Avg',
                'RH',
                'DewPt_Avg',
                'VaporPress_Avg',
                'WindSp_Avg',
                'WindDir_Avg',
                'JuddDepth_Avg',
                'PARIn_Avg',
                'PAROut_Avg',
                'SWOut_NR01_Avg',
                'SWIn_NR01_Avg',
                'NetRad_NR01_Avg',
                'LWOut_Cor_NR01_Avg',
                'LWIn_Cor_NR01_Avg',
                'Evapotrans_ETo',
                'Evapotrans_ETr',
                'VWC_5cm_Avg',
                'SoilTemp_5cm_Avg',
                'Permittivity_5cm_Avg',

                'VWC_10cm_Avg',
                'SoilTemp_10cm_Avg',
                'Permittivity_10cm_Avg',

                'VWC_20cm_Avg',
                'SoilTemp_20cm_Avg',
                'Permittivity_20cm_Avg',

                'VWC_50cm_Avg',
                'SoilTemp_50cm_Avg',
                'Permittivity_50cm_Avg',

                'VWC_100cm_Avg',
                'SoilTemp_100cm_Avg',
                'Permittivity_100cm_Avg'

            ]

            if database == 'iUTAH_Provo_OD':
                vars_to_show.insert(0, 'AirTemp_Avg')
                vars_to_show.insert(7, 'Rain_Tot')
            else:
                vars_to_show.insert(0, 'AirTemp_ST110_Avg')
                vars_to_show.insert(7, 'Precip_Tot_Avg')

        novars = True
        for var_sel in vars_to_show:
            var_print = next((var for var in variables if var.code == var_sel), None)

            if var_print is not None:
                novars = False
                file_str += "\t\t\t\t\t\t\t{\n"
                file_str += "\t\t\t\t\t\t\t\"name\": \""+ str(var_print.name) + "\",\n"
                file_str += "\t\t\t\t\t\t\t\"unit\": \"" + str(var_print.variable_unit.abbreviation)+ "\",\n"
                file_str += "\t\t\t\t\t\t\t\"code\": \"" + str(var_print.code)+ "\",\n"
                file_str += "\t\t\t\t\t\t\t\"sample\": \"" + str(var_print.sample_medium)+ "\",\n"
                file_str += "\t\t\t\t\t\t\t\"values\": ["
                
                #put variable values in here
                loginfo += "\t\t\t\t\t\t\t\t   Now getting values for "+ var_print.name +"\n"
                var_values = ss.get_ninety_six_values_by_site_id_and_var_id(site.id, var_print.id)
                threshold = 96
                if len(var_values) < threshold:
                    threshold = len(var_values)
                for x in range(0, threshold):
                    file_str += str(var_values[x].data_value)
                    if x != threshold-1:
                         file_str += ", "
                         
                file_str += "]\n"
                file_str += "\t\t\t\t\t\t\t}"
                #if variables[len(variables)-1].id != var.id:
                file_str += ",\n"
            else:
                loginfo += "\t\t\t\t\t\t\t\t\t   Var code \"" + var_sel + "\" not found in site: " + site.code

        if not novars:
            file_str = file_str[:-2]
            
        logger.info(loginfo)
        logger.info("Finished getting variables for site: " + site.name + " in " + database)
        file_str += "\n\t\t\t\t\t]\n\n"
        
        file_str += "\t\t\t}"
        if sites[len(sites)-1] != site:
            file_str += ","
        file_str += "\n\n"
    logger.info("Finished getting sites for " + database)
    text_file.write(file_str)
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


