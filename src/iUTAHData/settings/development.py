from iUTAHData.settings.base import *

#DATABASE_PATH = os.path.join(os.pardir, 'db.sqlite3')
#DATABASES['default']['NAME'] = DATABASE_PATH;

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DEBUG = True

SITE_ROOT = os.path.realpath(os.path.join(BASE_DIR, os.pardir))

STATIC_ROOT = os.path.join(SITE_ROOT, 'mdfserver', 'static')
STATIC_URL = '/static/'
BASE_URL = 'mdf/'
