"""
Django settings for mdfiutah project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Loads settings configuration data from settings.json file
data = {}
try:
    with open(os.path.join(BASE_DIR, 'settings', 'settings.json')) as data_file:
        data = json.load(data_file)
except IOError:
    print("You need to setup the settings data file (see instructions in base.py file.)")

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = data["secret_key"]
except KeyError:
    print("The secret key is required in the settings.json file.")
    exit(1)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mdfserver',
    'tinymce',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'iUTAHData.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iUTAHData.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {}
for database in data['databases']:
    DATABASES[database['name']] = {
        'ENGINE': database['engine'],
        'NAME': database['schema'],
        'USER': database['user'] if 'user' in database else '',
        'PASSWORD': database['password'] if 'password' in database else '',
        'HOST': database['host'] if 'host' in database else '',
        'PORT': database['port'] if 'port' in database else '',
        'OPTIONS': database['options'] if 'options' in database else {},
        'TEST': database['test'] if 'test' in database else {},
    }

    # Password validation
    # https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        # {
        #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        # },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        # {
        #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        # },
    ]


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