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

dump_location = "C:\\iUtahDataCollector\\DataParser\\tempfiles\\"
static_folder = "C:\inetpub\wwwroot\mdf\static\mdfserver\json"
log_file = "C:\\dataparserlog.txt"

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
        for var in variables:
            file_str += "\t\t\t\t\t\t\t{\n"
            file_str += "\t\t\t\t\t\t\t\"name\": \""+ str(var.name) + "\",\n"
            file_str += "\t\t\t\t\t\t\t\"unit\": \"" + str(var.variable_unit.abbreviation)+ "\",\n"
            file_str += "\t\t\t\t\t\t\t\"code\": \"" + str(var.code)+ "\",\n"
            file_str += "\t\t\t\t\t\t\t\"values\": [" 
            
            #put variable values in here
            loginfo += "\t\t\t\t\t\t\t\t   Now getting values for "+ var.name +"\n"
            var_values = ss.get_ten_values_by_site_id_and_var_id(site.id, var.id)
            for x in range(0, 10):
                file_str += str(var_values[x].data_value)
                if x != 9:
                     file_str += ", "
            
            file_str += "]\n"
            file_str += "\t\t\t\t\t\t\t}"
            if variables[len(variables)-1].id != var.id:
                file_str += ",\n"
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


def moveFile(src, dest):
    shutil.copy(src, dest)

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
    moveFile(dump_location + "LoganSite.json", static_folder)
    moveFile(dump_location + "ProvoSite.json", static_folder)
    moveFile(dump_location + "RedButteSite.json", static_folder)
    logger.info("Finished moving JSON files to static folder. ")
    logger.info("\n========================================================\n")

def databaseParser(database, location):
    logger.info("Started "+ location + " JSON File.")
    text_file = open(dump_location + location +"Site.json", "w")
    logger.info("Started creating " + location + " JSON file. ")
    #JSON File begins
    text_file.write("{\n")
    handleConnection(database, text_file)
    text_file.write("}")
    text_file.close()
    logger.info("Finished creating " + location + " JSON file. ")

dataParser()


