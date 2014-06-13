import sys
import os
import pyodbc

this_file = os.path.realpath(__file__)
directory = os.path.dirname(os.path.dirname(this_file))
sys.path.insert(0, directory)
from odmservices import ServiceManager
sm = ServiceManager()


def handleConnection(database):
    sm._current_connection= {'engine':'mssql', 'user':'webapplication' , 'password':'W3bAppl1c4t10n!', 'address':'iutahdbs.uwrl.usu.edu', 'db':database}
    ss = sm.get_series_service()
    sites = ss.get_all_sites()

    #lets print all the sites, shall we?
    for site in sites:
        text_file.write("\t\t\t\"" + str(site.code) +"\": {\n")
        #Print all info for each site here
        text_file.write("\t\t\t\t\t\"info\": {\n")
        text_file.write("\t\t\t\t\t\t\"code\": \""+ str(site.code) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"name\": \""+str(site.name) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"latitude\": \""+str(site.latitude) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"longitude\": \""+str(site.longitude) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"lat_long_datum\": \""+str(site.lat_long_datum_id) +"\",\n") #WTheck?
        text_file.write("\t\t\t\t\t\t\"elevation\": \""+str(site.elevation_m) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"local_x\": \""+str(site.local_x) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"local_y\": \""+str(site.local_y) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"local_projection\": \""+str(site.local_projection_id) +"\",\n") #WTheck?
        text_file.write("\t\t\t\t\t\t\"pos_accuracy\": \""+str(site.pos_accuracy_m) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"state\": \""+str(site.state) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"county\": \""+str(site.county) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"comments\": \""+str(site.comments) +"\",\n")
        text_file.write("\t\t\t\t\t\t\"type\": \""+str(site.type) +"\"\n")
        text_file.write("\t\t\t\t\t\t},\n\n")
        
        #print each variable and its value here, bye
        text_file.write("\t\t\t\t\t\"vars\": [\n")
        variables = ss.get_variables_by_site_code(site.code)
        for var in variables:
            text_file.write("\t\t\t\t\t\t\t\t{\n")
            text_file.write("\t\t\t\t\t\t\t\t\"name\": "+ str(var.name) + ",\n")
            text_file.write("\t\t\t\t\t\t\t\t\"unit\": " + str(var.variable_unit.abbreviation)+ ",\n")
            text_file.write("\t\t\t\t\t\t\t\t\"values\": [" )
            #put variable values in here
            #var_values = ss.get_all_values_by_var_id(var.id)
            #for x in range(0, 10):
            #    text_file.write(str(var_values[x].data_value) + ", ")
            #text_file.write("]\n")
            #text_file.write("\t\t\t\t\t\t\t\t}")
            #if variables[len(variables)-1].id != var.id:
            #    text_file.write(",\n")
        text_file.write("\n\t\t\t\t\t\t]\n\n")
        
        text_file.write("\t\t\t\t}")
        if sites[len(sites)-1] != site:
            text_file.write(",")
        text_file.write("\n\n")
        
    pass


with open("C:\\Output.txt", "w") as text_file:
    #JSON File begins
    text_file.write("{\n")
    
    #logan database is loaded here
    text_file.write("\t\"logan\": {\n")
    handleConnection('iUTAH_Logan_OD')

    text_file.write("\t\t},\n\n")

    #provo database is loaded here
    text_file.write("\t\"provo\": {\n")

    handleConnection('iUTAH_Provo_OD')

    text_file.write("\t\t},\n\n")

    #red butte creek database is loaded here
    text_file.write("\t\"red_butte\": {\n")
    handleConnection('iUTAH_RedButte_OD')

    text_file.write("\t\t}\n\n")

    text_file.write("}")


