"""
Django settings for mdfiutah project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+e0s9c#(oe-wi2*%dxl53eqcb+7&5w3r04-#f3f+cl-2f3#uk%'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mdfserver',
    'tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'iUTAHData.urls'

WSGI_APPLICATION = 'iUTAHData.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, os.pardir, os.pardir, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#TINYMCE_JS_URL = os.path.join(os.environ['APPL_VIRTUAL_PATH'] + "/", "static/mdfserver/js/tiny_mce/tiny_mce.js")
TINYMCE_JS_URL = os.path.join("/mdf/", "static/mdfserver/js/tiny_mce/tiny_mce.js")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "advlist,autosave,media",
    'theme': "advanced",
    'cleanup_on_startup': False,
    'custom_undo_redo_levels': 10,
	'relative_urls' : False,
    'content_css': "/mdf/static/mdfserver/css/bootstrap.css,/mdf/static/mdfserver/css/custom_style.css",
    }