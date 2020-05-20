from iUTAHData.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

if "host" in data:
    ALLOWED_HOSTS.append(data["host"])
if "host_alt" in data:
    ALLOWED_HOSTS.append(data["host_alt"])

SITE_URL = 'mdf/'
STATIC_ROOT = data["static_root"]
STATIC_URL = SITE_URL + data["static_url"]
