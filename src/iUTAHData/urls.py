from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from mdfserver import views

admin.autodiscover()

BASE_URL = settings.SITE_URL[1:]

urlpatterns = patterns('',
    url(r'^' + BASE_URL + 'admin/', include(admin.site.urls)),
    #url(r'^' + BASE_URL, include('mdfserver.urls')),
    (r'^' + BASE_URL + 'tinymce/', include('tinymce.urls')),
	url(r'^' + BASE_URL + '$', views.index, name='index'),
	url(r'^' + BASE_URL + 'index/', views.index, name='index'),
	url(r'^' + BASE_URL + 'river_info/(?P<database>[\w\s]*)/(?P<site_code>[\w\s]*[/]?)/$', views.river_dynamic, name='dynamic'),
	url(r'^' + BASE_URL + '(?P<pages_passed>[\w\s]*)/(?P<subpage>[\w\s]*[/]?)/$', views.subpages, name='subpages'),
	url(r'^' + BASE_URL + '(?P<pages_passed>[\w\s]*[/]?)/$', views.pages, name='pages')
)