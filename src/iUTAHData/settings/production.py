import sys
import django

from iUTAHData.settings.base import *

#For error logging (helicon zoo error trace logging doesn't work)
#sys.stderr = open('err.log', 'w')

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', data['host']]

SITE_ROOT = os.environ['APPL_PHYSICAL_PATH']
SITE_URL = os.environ['APPL_VIRTUAL_PATH'] + "/"

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = SITE_URL + 'static/'

django.setup()
