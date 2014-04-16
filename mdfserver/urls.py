__author__ = 'Mario'

from django.conf.urls import patterns, url

from mdfserver import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^index/', views.index, name='index'),
        url(r'^(?P<pages_passed>[\w\s]*)/(?P<subpage>[\w\s]*[/]?)/$', views.subpages, name='subpages'),
        url(r'^(?P<pages_passed>[\w\s]*[/]?)/$', views.pages, name='pages')
        #url(r'^(?P<pages>[^\s]+)/$', views.pages, name='pages')
)