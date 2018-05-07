import sys
import django

from iUTAHData.settings.base import *

#For error logging (helicon zoo error trace logging doesn't work)
#sys.stderr = open('err.log', 'w')

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', data['host']]

# On production, SITE_ROOT is the parent directory of the project (e.i. not /path/to/project/src)
SITE_ROOT = os.environ['APPL_PHYSICAL_PATH']
SITE_URL = os.environ['APPL_VIRTUAL_PATH'] + "/"

# NOTE: STATIC_ROOT on production is not located inside the project directory
STATIC_ROOT = os.path.join(SITE_ROOT, 'mdfserver', 'static')
STATIC_URL = SITE_URL + 'static/'

BASE_URL = 'mdf/'

django.setup()
