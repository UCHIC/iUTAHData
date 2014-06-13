import sys
import os
import pyodbc

this_file = os.path.realpath(__file__)
directory = os.path.dirname(os.path.dirname(this_file))
sys.path.insert(0, directory)
from odmservices import ServiceManager
sm = ServiceManager()

sm._current_connection= {'engine':'mssql', 'user':'webapplication' , 'password':'W3bAppl1c4t10n!', 'address':'iutahdbs.uwrl.usu.edu', 'db':'iUTAH_RedButte_OD'}
#conn = 'mssql:pyodbc//webapplication:w3bAppl1cat10n!@iutahdbs.uwrl.usu.edu/iUTAH_Logan_OD'
conn_dict = sm.get_current_connection()
#print conn_dict
#print sm.get_db_version(conn_dict)
ss= sm.get_series_service()

sites= ss.get_all_sites()
print "========================================================="
#print sites
#print sites[0].code

print dir(sites[0])
print sites[0].code
print sites[0].name
print sites[0].latitude
print sites[0].longitude
print sites[0].lat_long_datum_id #WTheck?
print sites[0].elevation_m
print sites[0].local_x
print sites[0].local_y
print sites[0].local_projection_id
print sites[0].pos_accuracy_m
print sites[0].state
print sites[0].county
print sites[0].comments
print "Red Butte Creek"
print sites[0].type


for site in sites:
    print site

with open("C:\\Output.txt", "w") as text_file:
    text_file.write("s0000ites")
    text_file.write("sds0000ites")
print "========================================================="
print "========================================================="
for site in sites:
    print "   "
    print "   "
    print "**********************************************************"
    print "Site: " + str(site)
    variables = ss.get_variables_by_site_code(site.code)
    for var in variables:
        print var

    print "**********************************************************"
#print "========================================================="