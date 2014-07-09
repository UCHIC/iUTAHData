from iUTAHData.settings.base import *

#DATABASE_PATH = os.path.join(os.pardir, 'db.sqlite3')
#DATABASES['default']['NAME'] = DATABASE_PATH;

DEBUG = True
TEMPLATE_DEBUG = True

STATIC_URL = '/static/'

SITE_URL = '/mdf/'

STATIC_ROOT = 'static/'
STATIC_URL = SITE_URL + 'static/'