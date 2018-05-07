from django.conf.urls import url

from .views import HomeView, DevelopmentView, DataManagementView, SoftwareDevelopmentView, \
    HardwareDevelopmentView, DataPolicyView, HouseholdSurveyView, GamutNetworkView, LoganRiverView, ProvoRiverView, \
    RedButteCreekView, HouseHoldQuestionnairesView, HouseHoldQuestionnairesEnglishView, \
    HouseHoldQuestionnairesSpanishView, DocumentationView, TrainingMaterialsView, PersonnelView, gamut_webcams_view, \
    river_dynamic

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^Development/$', DevelopmentView.as_view(), name='development'),
    url(r'^Development/data_management/$', DataManagementView.as_view(), name='data_management'),
    url(r'^Development/Software_Development/$', SoftwareDevelopmentView.as_view(), name='software_development'),
    url(r'^Development/Hardware_Development/$', HardwareDevelopmentView.as_view(), name='hardware_development'),
    url(r'^Data/Data_Policy/$', DataPolicyView.as_view(), name='data_policy'),
    url(r'^Data/household_survey/$', HouseholdSurveyView.as_view(), name='household_survey'),
    url(r'^Data/Gamut_Network/$', GamutNetworkView.as_view(), name='gamut_network'),
    url(r'^Data/Logan_River/$', LoganRiverView.as_view(), name='logan_river'),
    url(r'^Data/Provo_River/$', ProvoRiverView.as_view(), name='provo_river'),
    url(r'^Data/Red_Butte/$', RedButteCreekView.as_view(), name='red_butte_creek'),
    url(r'^Data/household_survey_instrument/$', HouseHoldQuestionnairesView.as_view(), name='household_questionnaries'),
    url(r'^Data/household_survey_instrument_English/$', HouseHoldQuestionnairesEnglishView.as_view(), name='household_questionnaires_en'),
    url(r'^Data/household_survey_instrument_Espanol/$', HouseHoldQuestionnairesSpanishView.as_view(), name='household_questionnaires_es'),
    url(r'^About/Documentation/$', DocumentationView.as_view(), name='documentation'),
    url(r'^About/Training_Materials/$', TrainingMaterialsView.as_view(), name='training_materials'),
    url(r'^About/Personnel/$', PersonnelView.as_view(), name='personnel'),
    url(r'^river_info/(?P<db_name>[\w\s]*)/(?P<site_code>[\w\s]*[/]?)/$', river_dynamic, name='dynamic'),
    url(r'^Data/Gamut_Webcams/.*$', gamut_webcams_view, name='gamut_webcams'),
]