import json
import re
import glob

import datetime
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http.response import Http404, JsonResponse
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

    with staticfiles_storage.open('mdfserver/json/%sSite.json' % network_map[database_name]) as river_data:
        json_data = json.load(river_data)
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
    deprecated_sites = {
        "RB_KF_BA": {
            "deprecation_time": 'August 8, 2016',
            "new_site_network": "iUTAH_RedButte_OD",
            "new_site_code": "RB_LKF_A"
        }
    }

    print(data_river)

    pics = []
    counter = 1
    while finders.find('mdfserver/images/site_images/' + database + '/' + site_code + '/Site (' + str(
            counter) + ').jpg') is not None:
        pics.append('Site (' + str(counter) + ').jpg')
        counter += 1

    xtra_site = "none"
    if site_code == "RB_ARBR_AA":
        xtra_site = data_river['RB_ARBR_USGS']
    elif site_code == "PR_BJ_AA":
        xtra_site = data_river['PR_BJ_CUWCD']
    elif site_code == "PR_CH_AA":
        xtra_site = data_river['PR_CH_CUWCD']
    elif site_code == "PR_LM_BA":
        xtra_site = data_river['PR_UM_CUWCD']

    sites_for_select = ['LR_Mendon_AA', 'LR_MainStreet_BA', 'LR_WaterLab_AA', 'LR_TG_BA', 'LR_FB_BA', 'LR_FB_C',
                        'LR_GC_C', 'LR_TG_C', 'LR_TWDEF_C', 'LR_Wilkins_R', 'BSF_CONF_BA',
                        'PR_BJ_AA', 'PR_CH_AA', 'PR_CH_C', 'PR_LM_BA', 'PR_BD_C', 'PR_ST_BA', 'PR_ST_C', 'PR_TL_C',
                        'RB_ARBR_AA', 'RB_CG_BA', 'RB_FD_AA', 'RB_KF_BA', 'RB_RBG_BA', 'RB_ARBR_C', 'RB_GIRF_C',
                        'RB_KF_C', 'RB_TM_C', 'RB_CR_SD', 'RB_Dent_SD', 'RB_FortD_SD', 'RB_GIRF_SD']

    db_sites = data_river.keys()
    approved_sites = []

    for variable in sites_for_select:
        var_print = next((var for var in db_sites if var == variable), None)
        if var_print is not None:
            approved_sites.append(variable)

    data_river = prepare_for_heading(data_river[site_code], "Soil")
    data_river = prepare_for_heading(data_river, "Air")

    data_river['active'] = site_code not in deprecated_sites
    data_river['deprecation_date'] = deprecated_sites[site_code]['deprecation_time'] if not data_river[
        'active'] else None
    data_river['new_site_network'] = deprecated_sites[site_code]['new_site_network'] if not data_river[
        'active'] else None
    data_river['new_site_code'] = deprecated_sites[site_code]['new_site_code'] if not data_river['active'] else None

    context = {'site': database,
               'river_data': data_river,
               'pics': pics,
               'xtra_site': xtra_site,
               'db_sites': approved_sites,
               'static_url': settings.STATIC_URL}
    return render(request, 'mdfserver/river_dynamic.html', context)


def gamut_webcams_view(request):
    gamut_webcam_dir = os.path.join(settings.STATIC_ROOT, 'mdfserver\\images\\gamutphotos\\')
    site_details = json.load(open(os.path.join(gamut_webcam_dir, 'webcam_details.json')))
    context = {'static_url': settings.STATIC_URL}
    photos_per_page = 8

    if request.is_ajax():
        if 'site' in request.GET and 'network' in request.GET:
            site = request.GET.get('site')
            network = request.GET.get('network')
            index = int(request.GET.get('index'))
            folder = site_details[network][site]['img_dir']

            context['site_selected'] = site
            context['site_name'] = site_details[network][site]['site_name']
            context['network'] = network
            context['index'] = index
            context['img_dir'] = folder
            # context['img_name'] = site_details[network][site]['img_name']
            # context['img_date'] = site_details[network][site]['img_date']

            ordered_files = json.load(open(os.path.join(gamut_webcam_dir, 'ordered_dir_listings.json')))
            photo_count = len(ordered_files[folder])
            first_index = photos_per_page * index if (index * photos_per_page < photo_count) else None
            last_index = photos_per_page * (index + 1) if (photos_per_page * (index + 1) < photo_count) else -1

            if first_index is not None:
                context['next_photos'] = ordered_files[folder][first_index:last_index]
                context['img_name'] = context['next_photos'][0]['name']
                context['img_date'] = context['next_photos'][0]['date']
                context['end_of_list'] = len(context['next_photos']) < photos_per_page
                return render(request, 'mdfserver/data/image_overlay.html', context)
            return Http404
    else:
        context['networks'] = site_details
        return render(request, 'mdfserver/data/gamut_webcams.html', context)
