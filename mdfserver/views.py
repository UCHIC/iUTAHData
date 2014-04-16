from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from mdfserver.models import Page, Subpage

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