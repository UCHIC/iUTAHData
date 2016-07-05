from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from mdfserver import views
from mdfserver.views import HomeView, DevelopmentView, DataManagementView, SoftwareDevelopmentView

admin.autodiscover()

BASE_URL = settings.SITE_URL[1:]

urlpatterns = [
    url(r'^' + BASE_URL + '$', HomeView.as_view(), name='index'),
    url(r'^' + BASE_URL + 'Development/$', DevelopmentView.as_view(), name='development'),
    url(r'^' + BASE_URL + 'Development/data_management/$', DataManagementView.as_view(), name='data_management'),
    url(r'^' + BASE_URL + 'Development/Software_Development/$', SoftwareDevelopmentView.as_view(), name='software_development'),


    # url(r'^' + BASE_URL + 'admin/', include(admin.site.urls)),
    # # url(r'^' + BASE_URL, include('mdfserver.urls')),
    # url(r'^' + BASE_URL + 'tinymce/', include('tinymce.urls')),
    # url(r'^' + BASE_URL + '$', views.index, name='index'),
    # url(r'^' + BASE_URL + 'index/', views.index, name='index'),
    # url(r'^' + BASE_URL + 'river_info/(?P<database>[\w\s]*)/(?P<site_code>[\w\s]*[/]?)/$', views.river_dynamic,
    #     name='dynamic'),
    # url(r'^' + BASE_URL + '(?P<pages_passed>[\w\s]*)/(?P<subpage>[\w\s]*[/]?)/$', views.subpages, name='subpages'),
    # url(r'^' + BASE_URL + '(?P<pages_passed>[\w\s]*[/]?)/$', views.pages, name='pages')
]
