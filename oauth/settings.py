# -*- coding: utf-8 -*-
"""
Django settings for oauth project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#2&mi$@f5p@v+vo5mngau-1e!ta%h6y)h0%4m*eg@ux^%s89f%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ "*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'appuser', 
    'apps',
)
CORS_ORIGIN_WHITELIST = ( '127.0.0.1',  'http://www.asucast.com:8080', 'www.asucast.com:8080','http://47.95.239.228:8800','47.95.239.228:8800')
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'oauth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'oauth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'oauth',
		'USER':'root',
        'PASSWORD':'sqlroot',
        'HOST':'localhost',
        'PORT':3306, 
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
AUTH_USER_MODEL = 'appuser.AdaptorUser'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
)

LOGIN_URL = '/users/login/'


EMAIL_SWITCH = True 
SMTP_SERVER         ='smtp.mxhichina.com' #SMTP server IP address
SMTP_SERVER_USER    ='postmaster@map2family.com'  
SMTP_SERVER_PWD     ='Kkikkm889886'  
"""
SMTP_SERVER         ='smtp.163.com' #SMTP server IP address
SMTP_SERVER_USER    ='281475120@163.com'  
SMTP_SERVER_PWD     ='163889886'  
"""
PROJECTNAME = '一数科技'


SMS = {
    'SMS_SN' : "SDK-BBX-010-22746",
    'SMS_PWD' : "76D7DAAC410AF587F0DEEE4F5FA86795",
}
SMS_API = "http://sdk2.entinfo.cn:8061/mdsmssend.ashx?sn=SDK-BBX-010-22746&pwd=76D7DAAC410AF587F0DEEE4F5FA86795&mobile={0}&content={1}"
