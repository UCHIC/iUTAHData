# coding=utf-8
import json
import re
import glob
import requests
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


class MDFBaseView(TemplateView):
    pass

class HomeView(MDFBaseView):
    template_name = 'mdfserver/index.html'


class DevelopmentView(MDFBaseView):
    template_name = 'mdfserver/development/development.html'


class DataManagementView(MDFBaseView):
    template_name = 'mdfserver/development/data_management.html'


class SoftwareDevelopmentView(MDFBaseView):
    template_name = 'mdfserver/development/software_development.html'


class HardwareDevelopmentView(MDFBaseView):
    template_name = 'mdfserver/development/hardware_development.html'


class DataPolicyView(MDFBaseView):
    template_name = 'mdfserver/data/data_policy.html'


class HouseholdSurveyView(MDFBaseView):
    template_name = 'mdfserver/data/household_survey.html'


class GamutNetworkView(MDFBaseView):
    template_name = 'mdfserver/data/gamut_network.html'


class BaseRiverView(MDFBaseView):
    db_name = None

    def get_sites_by_type(self, sites, type_, order_by='elevation', reverse=True):
        # filter out sites by type and restructure data to use for template
        sites = [{'site_code': code, 'data': value} for code, value in sites.iteritems()
                 if value['info']['type'] == type_]

        # sort sites before returning
        sites.sort(key=lambda site: site['data']['info'][order_by], reverse=reverse)

        return sites

    def get_context_data(self, **kwargs):
        context = super(BaseRiverView, self).get_context_data(**kwargs)

        context['db_name'] = self.db_name

        sites = deserialize_json(self.db_name)

        context['climate_sites'] = self.get_sites_by_type(sites, 'Atmosphere')
        context['aquatic_sites'] = self.get_sites_by_type(sites, 'Stream')
        context['storm_drain_sites'] = self.get_sites_by_type(sites, 'Storm sewer')

        return context


class LoganRiverView(BaseRiverView):
    template_name = 'mdfserver/data/logan_river.html'
    db_name = 'iUTAH_Logan_OD'


class ProvoRiverView(BaseRiverView):
    template_name = 'mdfserver/data/provo_river.html'
    db_name = 'iUTAH_Provo_OD'


class RedButteCreekView(BaseRiverView):
    template_name = 'mdfserver/data/red_butte_creek.html'
    db_name = 'iUTAH_RedButte_OD'


class HouseHoldQuestionnairesView(MDFBaseView):
    template_name = 'mdfserver/data/household_questionnaires.html'


class HouseHoldQuestionnairesEnglishView(MDFBaseView):
    template_name = 'mdfserver/data/household_questionnaires_en.html'


class HouseHoldQuestionnairesSpanishView(MDFBaseView):
    template_name = 'mdfserver/data/household_questionnaires_es.html'


class DocumentationView(MDFBaseView):
    template_name = 'mdfserver/about/documentation.html'


class TrainingMaterialsView(MDFBaseView):
    template_name = 'mdfserver/about/training_materials.html'


class PersonnelView(MDFBaseView):
    template_name = 'mdfserver/about/personnel.html'


# noinspection PyNonAsciiChar
def deserialize_json(database_name):
    network_map = {
        'iUTAH_Logan_OD': 'Logan',
        'iUTAH_Provo_OD': 'Provo',
        'iUTAH_RedButte_OD': 'RedButte'
    }

    # I know this is terrible... but so was this project before I ever touched it.
    retired_sites = ['PR_BD_C', 'PR_TL_C', 'PR_BJ_AA', 'PR_CH_AA', 'PR_LM_BA', 'PR_SageCreek_canal', 'PR_Flood_canal',
                     'RB_KF_BA']
    non_displayed_sites = ['RB_KF_S', 'RB_ARBR_USGS', 'PR_WD_USGS', 'PR_BJ_CUWCD', 'PR_UM_CUWCD', 'PR_CH_CUWCD',
                           'PR_HD_USGS', 'LR_Mendon_AA']

    with staticfiles_storage.open('mdfserver/json/%sSite.json' % network_map[database_name]) as river_data:
        json_data = json.load(river_data)

    # set site status
    for key, value in json_data.iteritems():
        value['info']['status'] = 'Retired' if key in retired_sites else 'Operational'
    # remove non-displayed-sites
    json_data = {key: value for key, value in json_data.iteritems() if key not in non_displayed_sites}

    def filter_duplicates(variables):
        new_vars = list()
        for var in variables:
            code_occurance = [x['code'] for x in new_vars if x['code'] == var['code']]
            if len(code_occurance) < 1:
                new_vars.append(var)
        return new_vars

    # remove duplicate variables... because they exist for some reason... ¯\_(ツ)_/¯
    for key, value in json_data.iteritems():
        value['vars'] = filter_duplicates(value['vars'])

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


def river_dynamic(request, db_name, site_code):
    data_river = deserialize_json(db_name)
    deprecated_sites = {
        "RB_KF_BA": {
            "deprecation_time": 'August 8, 2016',
            "new_site_network": "iUTAH_RedButte_OD",
            "new_site_code": "RB_LKF_A"
        }
    }

    pics = []
    photo_dir = finders.find('mdfserver/images/site_images/{0}/{1}/'.format(db_name, site_code))
    image_filenames = [photo for photo in os.listdir(photo_dir)] if photo_dir is not None else list()
    for filename in image_filenames:
        if re.match(r'.*\.(jpg|png)$', filename, re.IGNORECASE):
            pics.append(filename)

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

    def filter_variable_code(var, code):
        return var.get('code', '') != code

    # filter out 'DewPt_Avg' variable from climate sites (i.e. data_river['info']['type'] == Atmosphere)
    if data_river['info']['type'] == 'Atmosphere':
        data_river['vars'] = filter(lambda var: filter_variable_code(var, 'DewPt_Avg'), data_river['vars'])

    # filter out 'ODO_Sat' variable from aquate sites (i.e. data_river['info']['type'] == Stream)
    if data_river['info']['type'] == 'Stream':
        data_river['vars'] = filter(lambda var: filter_variable_code(var, 'ODO_Sat'), data_river['vars'])

    context = {'site': db_name,
               'river_data': data_river,
               'pics': pics,
               'xtra_site': xtra_site,
               'db_sites': approved_sites,
               'static_url': settings.STATIC_URL}
    return render(request, 'mdfserver/river_dynamic.html', context)


def gamut_webcams_view(request):
    # Using the 'requests' library is just temporary until data.iutahepscor.org is moved permanently over to the linux server
    req = requests.request('GET', 'http://data.iutahepscor.org/mdf/static/mdfserver/images/gamutphotos/webcam_details.json')
    site_details = req.json()
    context = {'static_url': "http://data.iutahepscor.org/mdf/static/mdfserver/images/gamutphotos"}

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

            req = requests.request('GET', 'http://data.iutahepscor.org/mdf/static/mdfserver/images/gamutphotos/ordered_dir_listings.json')
            ordered_files = req.json()

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
