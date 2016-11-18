from iUTAHData.settings.base import *

#DATABASE_PATH = os.path.join(os.pardir, 'db.sqlite3')
#DATABASES['default']['NAME'] = DATABASE_PATH;

DEBUG = True

SITE_ROOT = os.path.join(BASE_DIR, os.pardir)

STATIC_ROOT = os.path.join(SITE_ROOT, 'mdfserver', 'static')
STATIC_URL = '/static/'
SITE_URL = ''
