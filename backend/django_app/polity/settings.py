"""
Django settings for polity project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
# for db environment settings
import os

from pathlib import Path

# ***********************************************************************************************
# get environmental variables

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# 'ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# ***********************************************************************************************

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition

INSTALLED_APPS = [
    # start django-admin-interface
    'admin_interface',
    'colorfield',
    # end django-admin-interface
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # for allauth
    'django.contrib.sites', 
    # for spatialite
    'django.contrib.gis', 

    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'location_field.apps.DefaultConfig',
    
    # DRF
    'rest_framework',
    'rest_framework.authtoken',

    # local
    'users.apps.UsersConfig',
    'locations.apps.LocationsConfig',
    'legislatives.apps.LegislativesConfig',
    'politicans.apps.PoliticansConfig',
    'parties.apps.PartiesConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'polity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'polity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# PostgreSQL + PostGIS 
# dependency: pipenv install psycopg2
# note default values
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE", "django.contrib.gis.db.backends.spatialite"),
        'NAME': os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        'USER': os.environ.get("SQL_USER", "user"),
        'PASSWORD': os.environ.get("SQL_PASSWORD", "password"),
        'HOST': os.environ.get("SQL_HOST", "localhost"),
        'PORT': os.environ.get("SQL_PORT", "5432"),
    }
}

# only for spatiallite, if no postgis is present
SPATIALITE_LIBRARY_PATH = 'mod_spatialite.so'



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zurich'

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ***********************************************************************************************
# FILE HANDLING
# ***********************************************************************************************

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# ***********************************************************************************************
# CUSTOM USER MODEL
# ***********************************************************************************************

AUTH_USER_MODEL = 'users.CustomUser'

# Custom Serializer for CustomUser
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.api.serializers.CustomUserDetailSerializer',
}

# ***********************************************************************************************
# PLUGINS
# ***********************************************************************************************


# PLUGIN: Site-ID for Registration @dj-rest-auth AND (dependency) allauth
SITE_ID = 1

# PLUGIN: DRF
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.SessionAuthentication', #only for dev
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
    # for production: disable browsable api
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ],
}

# # PLUGIN: JWT
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'polity-jwt'


# PLUGIN: django-location-field
LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'search.provider': 'nominatim',
}

# PLUGIN: django-admin-interface
X_FRAME_OPTIONS='SAMEORIGIN' # only if django version >= 3.0