"""
Django settings for fiscalizacion project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_BASE = os.path.join(os.environ['USERPROFILE'])

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g8vl+!lty%f^yot$%dj)3xaaq)kr+5v(i9p7%-d5+k+106=ts@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'rest_framework',
    'django_filters',
    # 'bootstrap_datepicker_plus',
    #'bootstrap_datepicker', #pip install django-bootstrap-datepicker-widget
    #'bootstrap3_datetime', #pip install django-bootstrap3-datetimepicker
    'apps.r132',
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

ROOT_URLCONF = 'fiscalizacion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [os.path.join(BASE_DIR, 'templates/materializecss')],
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

WSGI_APPLICATION = 'fiscalizacion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(os.environ['USERPROFILE'], 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'HOST': 'WIN7-PC\\SQLEXPRESS',
#         'PORT': '1433',
#         'NAME': 'otra4',
#         'USER': 'sa',
#         'PASSWORD': '123456',
#         'OPTIONS': {
#             #'driver': 'SQL Server',
#             #'TDS_Version': '8.0',
#             'driver': 'ODBC Driver 13 for SQL Server',
#             #'unicode_results': True,
#             #'host_is_server': True,
            
#             #'SERVER': 'WIN7-PC\\SQLEXPRESS',
#             #'use_mars': True,
#             #"provider" : "SQLNCLI11",
#             #"extra_params" : "MARS Connection=True",
#             "extra_params": 'SERVER=WIN7-PC\\SQLEXPRESS;DATABASE=otra4;TDS_Version=8.0;'
#             #"extra_params": 'SERVER=WIN7-PC\\SQLEXPRESS;DATABASE=otra4;TDS_Version=8.0;Trusted_Connection=yes;'
#            # "extra_params":'TDS_Version=8.0'
#         },
#     },
# }
# DATABASE_CONNECTION_POOLING = False


# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'HOST': 'WIN7-PC\\SQLEXPRESS',
#         'PORT': '1433',
#         'NAME': 'otra4',
#         'USER': 'sa',
#         'PASSWORD': '123456',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 13 for SQL Server',
#             # "extra_params": 'SERVER=WIN7-PC\\SQLEXPRESS;DATABASE=otra4;TDS_Version=8.0;'
#             "extra_params": 'SERVER=WIN7-PC\\SQLEXPRESS;DATABASE=otra4;TDS_Version=8.0;Trusted_Connection=yes;'
#            # "extra_params":'TDS_Version=8.0'
#         },
#     },
# }
# DATABASE_CONNECTION_POOLING = False


# MS SQLEXPRESS ############################################# OK

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'WIN7-PC\\SQLEXPRESS',
        'PORT': '1433',
        'NAME': 'r132',
        'USER': 'sa',
        'PASSWORD': '123456',
        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
            # "extra_params": 'SERVER=WIN7-PC\\SQLEXPRESS;DATABASE=otra4;TDS_Version=8.0;'
            "extra_params": 'SERVER=WIN7-PC\\SQLEXPRESS;DATABASE=otra4;TDS_Version=8.0;Trusted_Connection=yes;'
           # "extra_params":'TDS_Version=8.0'
        },
    },
}
DATABASE_CONNECTION_POOLING = False


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# REST_FRAMEWORK = {
#     'PAGE_SIZE':10
# }

# REST_FRAMEWORK = {
#     # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
#     'PAGE_SIZE': 10
# }


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#STATIC_URL = '/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'static_files'),
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static'),
)
