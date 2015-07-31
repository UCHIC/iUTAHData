import json

from iUTAHData.settings.base import *
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from mdfserver.models import Page, Subpage

# Getting dynamic content when
def deserializeJSON(database):
    if database == 'iUTAH_Logan_OD':
        fileselection = 'Logan'
    else:
        if database == 'iUTAH_Provo_OD':
            fileselection = 'Provo'
        else:
            if database == 'iUTAH_RedButte_OD':
                fileselection = 'RedButte'

    river_data = open(BASE_DIR + '/../mdfserver/static/mdfserver/json/' + fileselection + 'Site.json')
    data = json.load(river_data)
    river_data.close()

    return data

def prepareForHeading(river_data, type):
    found = False
    for idx, variables in enumerate(river_data['vars']):
        if(variables['sample'] == type and not found):
            found = True
        else:
            if(variables['sample'] == type and found):
                river_data['vars'][idx]['sample'] = type + "_f"
    return river_data



def index(request):
    pages_in_server = Page.objects.all().order_by('-title')[:5]
    context = {'pages': pages_in_server}
    return render(request, 'mdfserver/main_template.html', context)

def pages(request, pages_passed):
    pages_in_server = Page.objects.all().order_by('-title')[:5]
    context = {'pages': pages_in_server, 'requested': pages_passed}
    return render(request, 'mdfserver/main_template.html', context)

def subpages(request, pages_passed, subpage):
    pages_in_server = Page.objects.all().order_by('-title')[:5]
    context = {'pages': pages_in_server, 'requested': pages_passed, 'subpage_name': subpage}
    return render(request, 'mdfserver/main_template.html', context)

def river_dynamic(request, database, site_code):
    data_river = deserializeJSON(database)
    pages_in_server = Page.objects.all().order_by('-title')[:5]
    pics = []
    counter = 1
    while finders.find('mdfserver/img/'+ database + '/'+site_code+'/Site'+ str(counter)+'.jpg') != None:
        pics.append('Site'+str(counter)+'.jpg')
        counter += 1

    xtra_site = "none"
    if site_code == "RB_ARBR_AA":
        xtra_site = data_river['RB_ARBR_USGS']
    else:
        if site_code == "PR_BJ_AA":
            xtra_site = data_river['PR_BJ_CUWCD']
        else:
            if site_code == "PR_CH_AA":
                xtra_site = data_river['PR_CH_CUWCD']
            else:
                if site_code == "PR_LM_BA":
                    xtra_site = data_river['PR_UM_CUWCD']


    sites_for_select = ['LR_Mendon_AA',	'LR_MainStreet_BA', 'LR_WaterLab_AA', 'LR_TG_BA', 'LR_FB_BA', 'LR_FB_C',
                        'LR_GC_C',	'LR_TG_C', 'LR_TWDEF_C', 'LR_Wilkins_R',
                        'PR_BJ_AA', 'PR_CH_AA', 'PR_CH_C', 'PR_LM_BA', 'PR_BD_C', 'PR_ST_BA',  'PR_ST_C', 'PR_TL_C',
                        'RB_ARBR_AA', 'RB_CG_BA', 'RB_FD_AA', 'RB_KF_BA', 'RB_RBG_BA', 'RB_ARBR_C', 'RB_GIRF_C',
                        'RB_KF_C', 'RB_TM_C', 'RB_CR_SD', 'RB_Dent_SD', 'RB_FortD_SD', 'RB_GIRF_SD']

    db_sites = data_river.keys()
    approved_sites = [];

    for variab in sites_for_select:
        var_print = next((var for var in db_sites if var == variab), None)
        if var_print is not None:
            approved_sites.append(variab)

    data_river = prepareForHeading(data_river[site_code], "Soil")
    data_river = prepareForHeading(data_river, "Air")
    context = {'pages': pages_in_server, 'site': database, 'river_data': data_river, 'pics': pics, 'xtra_site': xtra_site, 'db_sites': approved_sites }
    return render(request, 'mdfserver/river_dynamic.html', context)

