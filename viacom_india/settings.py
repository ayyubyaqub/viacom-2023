"""
Django settings for viacom_india project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import django
import os
from pathlib import Path
# from secret import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "QZ3moS1F2MkMIM2ahgx2UuNt1Gk4taRtvZP6TdL9uLU="
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['www.viacomindia.in', 'viacomindia.in', 'viacomindia.com', 'https://viacomindia.com' , 'http://viacomindia.com' , 'https://www.viacomindia.com' , 'http://www.viacomindia.com','www.viacomindia.com',
                 '.herokuapp.com', 'viacomindia.com', 'localhost', '127.0.0.1' , '43.204.239.248'
                 ]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",'www.viacomindia.in', 'viacomindia.in', 'viacomindia.com', 'https://viacomindia.com' , 'http://viacomindia.com' , 'https://www.viacomindia.com' , 'http://www.viacomindia.com','www.viacomindia.com',
                 '.herokuapp.com', 'viacomindia.com', 'localhost', '127.0.0.1' , '43.204.239.248'
]



DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 700
    }
}


# Application definition

INSTALLED_APPS = [
    'clearcache',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # Apps created
    'home',
    'categories',
    'subscription',
    'clients',
    'works',
    'blogs',
    'stories',
    'djrichtextfield',
    'dare2creative',
    'other_services',
    'django_social_share',
    'vi_network'
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = 'viacom_india.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'viacom_india.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "postgres",
        'USER': "postgres",
        'PASSWORD': "Mukeshahir$ayviacom",
        'HOST': "database-1.cl3rooputcor.ap-south-1.rds.amazonaws.com",
        'PORT': 5432,

        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': "ddc2j0bjgbt5ch",
        # 'USER': "ojusybbvvppzdf",
        # 'PASSWORD': "9a3d56257539f956759722a91f2789820f28819365ab8b1901a0c275865a5c95",
        # 'HOST': "ec2-52-70-186-184.compute-1.amazonaws.com",
        # 'PORT': 5432,

        
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     },
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         'TIMEOUT' : 3600*24*30,
#         'LOCATION': 'redis://127.0.0.1:6379',
#     }
# }

# CACHE_MIDDLEWARE_ALIAS="nothing"
CACHE_MIDDLEWARE_SECONDS=3600*24*30


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)

# # aws
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# =============================================================

# AWS_ACCESS_KEY_ID = 'AKIAWYSHDL6J76GELJ6H'
# AWS_SECRET_ACCESS_KEY = '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'
AWS_ACCESS_KEY_ID='AKIAWYSHDL6J76GELJ6H'
AWS_SECRET_ACCESS_KEY='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'
AWS_STORAGE_BUCKET_NAME = 'viacomindia'
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH= False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = "us-east-2"
AWS_S3_HOST = "s3.us-east-2.amazonaws.com"

# aws
# =====================================
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# import django_heroku
# django_heroku.settings(locals())

# EMAIL CONFIGURE
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = "viacomindiavideo@gmail.com"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = "lktdcismmsrrshgj"


CSRF_TRUSTED_ORIGINS=['https://viacomindia.com']