from django.conf import settings
from django.conf.urls import url, include

from django.contrib import admin

admin.autodiscover()

BASE_URL = settings.BASE_URL

urlpatterns = [
    url(r'^' + BASE_URL, include('mdfserver.urls'))
]
