from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from mdfserver import views
from mdfserver.views import HomeView, DevelopmentView, DataManagementView, SoftwareDevelopmentView, \
    HardwareDevelopmentView, DataPolicyView, HouseholdSurveyView, GamutNetworkView, LoganRiverView, ProvoRiverView, \
    RedButteCreekView, HouseHoldQuestionnairesView, HouseHoldQuestionnairesEnglishView, \
    HouseHoldQuestionnairesSpanishView, DocumentationView, TrainingMaterialsView, PersonnelView

admin.autodiscover()

BASE_URL = settings.SITE_URL[1:]

urlpatterns = [
    url(r'^' + BASE_URL + '$', HomeView.as_view(), name='index'),

    url(r'^' + BASE_URL + 'Development/$', DevelopmentView.as_view(), name='development'),
    url(r'^' + BASE_URL + 'Development/data_management/$', DataManagementView.as_view(), name='data_management'),
    url(r'^' + BASE_URL + 'Development/Software_Development/$', SoftwareDevelopmentView.as_view(), name='software_development'),
    url(r'^' + BASE_URL + 'Development/Hardware_Development/$', HardwareDevelopmentView.as_view(), name='hardware_development'),

    url(r'^' + BASE_URL + 'Data/Data_Policy/$', DataPolicyView.as_view(), name='data_policy'),
    url(r'^' + BASE_URL + 'Data/household_survey/$', HouseholdSurveyView.as_view(), name='household_survey'),
    url(r'^' + BASE_URL + 'Data/Gamut_Network/$', GamutNetworkView.as_view(), name='gamut_network'),
    url(r'^' + BASE_URL + 'Data/Logan_River/$', LoganRiverView.as_view(), name='logan_river'),
    url(r'^' + BASE_URL + 'Data/Provo_River/$', ProvoRiverView.as_view(), name='provo_river'),
    url(r'^' + BASE_URL + 'Data/Red_Butte/$', RedButteCreekView.as_view(), name='red_butte_creek'),
    url(r'^' + BASE_URL + 'Data/household_survey_instrument/$', HouseHoldQuestionnairesView.as_view(), name='household_questionnaries'),
    url(r'^' + BASE_URL + 'Data/household_survey_instrument_English/$', HouseHoldQuestionnairesEnglishView.as_view(), name='household_questionnaires_en'),
    url(r'^' + BASE_URL + 'Data/household_survey_instrument_Espanol/$', HouseHoldQuestionnairesSpanishView.as_view(), name='household_questionnaires_es'),

    url(r'^' + BASE_URL + 'About/Documentation/$', DocumentationView.as_view(), name='documentation'),
    url(r'^' + BASE_URL + 'About/Training_Materials/$', TrainingMaterialsView.as_view(), name='training_materials'),
    url(r'^' + BASE_URL + 'About/Personnel/$', PersonnelView.as_view(), name='personnel'),
    url(r'^' + BASE_URL + 'river_info/(?P<database>[\w\s]*)/(?P<site_code>[\w\s]*[/]?)/$', views.river_dynamic, name='dynamic'),
]
