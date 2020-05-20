from django.conf import settings
from django.conf.urls import url, include

from django.contrib import admin

admin.autodiscover()

SITE_URL = settings.SITE_URL

urlpatterns = [
    url(r'^' + SITE_URL, include('mdfserver.urls'))
]
