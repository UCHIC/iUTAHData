import json

from iUTAHData.settings.base import *
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.http import HttpResponse
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
    context = {'pages': pages_in_server, 'site': database, 'river_data': data_river[site_code], 'site_code': site_code }
    return render(request, 'mdfserver/river_dynamic.html', context)

