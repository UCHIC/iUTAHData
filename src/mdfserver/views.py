import json

from django.views.generic.base import TemplateView

from iUTAHData.settings.base import *
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.http import HttpResponse
from django.contrib.staticfiles import finders


class HomeView(TemplateView):
    template_name = 'mdfserver/index.html'


class DevelopmentView(TemplateView):
    template_name = 'mdfserver/development/development.html'


class DataManagementView(TemplateView):
    template_name = 'mdfserver/development/data_management.html'


class SoftwareDevelopmentView(TemplateView):
    template_name = 'mdfserver/development/software_development.html'


class HardwareDevelopmentView(TemplateView):
    template_name = 'mdfserver/development/hardware_development.html'


class DataPolicyView(TemplateView):
    template_name = 'mdfserver/data/data_policy.html'


class HouseholdSurveyView(TemplateView):
    template_name = 'mdfserver/data/household_survey.html'


class GamutNetworkView(TemplateView):
    template_name = 'mdfserver/data/gamut_network.html'


class LoganRiverView(TemplateView):
    template_name = 'mdfserver/data/logan_river.html'


class ProvoRiverView(TemplateView):
    template_name = 'mdfserver/data/provo_river.html'


class RedButteCreekView(TemplateView):
    template_name = 'mdfserver/data/red_butte_creek.html'


class HouseHoldQuestionnairesView(TemplateView):
    template_name = 'mdfserver/data/household_questionnaires.html'


class HouseHoldQuestionnairesEnglishView(TemplateView):
    template_name = 'mdfserver/data/household_questionnaires_en.html'


class HouseHoldQuestionnairesSpanishView(TemplateView):
    template_name = 'mdfserver/data/household_questionnaires_es.html'


class DocumentationView(TemplateView):
    template_name = 'mdfserver/about/documentation.html'


class TrainingMaterialsView(TemplateView):
    template_name = 'mdfserver/about/training_materials.html'


class PersonnelView(TemplateView):
    template_name = 'mdfserver/about/personnel.html'


def deserialize_json(database_name):
    network_map = {
        'iUTAH_Logan_OD': 'Logan',
        'iUTAH_Provo_OD': 'Provo',
        'iUTAH_RedButte_OD': 'RedButte'

    }

    # damn son...
    # i'm commenting and not deleting this for no reason.

    # if database == 'iUTAH_Logan_OD':
    #     fileselection = 'Logan'
    # else:
    #     if database == 'iUTAH_Provo_OD':
    #         fileselection = 'Provo'
    #     else:
    #         if database == 'iUTAH_RedButte_OD':
    #             fileselection = 'RedButte'

    river_data = open(BASE_DIR + '/../mdfserver/static/mdfserver/json/' + network_map[database_name] + 'Site.json')
    json_data = json.load(river_data)
    river_data.close()
    return json_data


def prepare_for_heading(river_data, type):
    found = False
    for idx, variables in enumerate(river_data['vars']):
        if variables['sample'] == type and not found:
            found = True
        else:
            if variables['sample'] == type and found:
                river_data['vars'][idx]['sample'] = type + "_f"
    return river_data


def river_dynamic(request, database, site_code):
    data_river = deserialize_json(database)
    pics = []
    counter = 1
    while finders.find('mdfserver/images/site_images/' + database + '/' + site_code + '/Site' + str(counter) + '.jpg') is not None:
        pics.append('Site' + str(counter) + '.jpg')
        counter += 1

    # i'm not even gonna try here...
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

    sites_for_select = ['LR_Mendon_AA', 'LR_MainStreet_BA', 'LR_WaterLab_AA', 'LR_TG_BA', 'LR_FB_BA', 'LR_FB_C',
                        'LR_GC_C', 'LR_TG_C', 'LR_TWDEF_C', 'LR_Wilkins_R',
                        'PR_BJ_AA', 'PR_CH_AA', 'PR_CH_C', 'PR_LM_BA', 'PR_BD_C', 'PR_ST_BA', 'PR_ST_C', 'PR_TL_C',
                        'RB_ARBR_AA', 'RB_CG_BA', 'RB_FD_AA', 'RB_KF_BA', 'RB_RBG_BA', 'RB_ARBR_C', 'RB_GIRF_C',
                        'RB_KF_C', 'RB_TM_C', 'RB_CR_SD', 'RB_Dent_SD', 'RB_FortD_SD', 'RB_GIRF_SD']

    db_sites = data_river.keys()
    approved_sites = []

    # this comment has no other purpose but to point out that, for some reason that's beyond be, there was a variable called variab here. it was just 2 letters away from kinda making sense...
    for variable in sites_for_select:
        var_print = next((var for var in db_sites if var == variable), None)
        if var_print is not None:
            approved_sites.append(variable)

    data_river = prepare_for_heading(data_river[site_code], "Soil")
    data_river = prepare_for_heading(data_river, "Air")

    context = {'site': database, 'river_data': data_river, 'pics': pics,
               'xtra_site': xtra_site, 'db_sites': approved_sites, 'static_url': settings.STATIC_URL}
    return render(request, 'mdfserver/river_dynamic.html', context)
