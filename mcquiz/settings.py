"""
Django settings for mcquiz project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open('../../key/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = [
    TEMPLATE_PATH   
]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

#email
with open('../../../../dbParams/mail.txt') as f:
    mailparams = [line.rstrip('\n') for line in f]
    
ALLOWED_HOSTS = [mailparams[0]]

EMAIL_HOST = mailparams[1]

EMAIL_PORT = mailparams[2]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mcquiz',
    'geographyquiz',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #The below middleware can't be used with Django 1.6
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



ROOT_URLCONF = 'mcquiz.urls'

#WSGI_APPLICATION = 'mcquiz.wsgi.application'


# Database
with open('../../../../dbParams/dbparams.txt') as f:
    dbparams = [line.rstrip('\n') for line in f]

DATABASES = {
    'default': {
        'ENGINE': dbparams[0],
        'NAME': dbparams[1],
        'USER': dbparams[2],
        'PASSWORD': dbparams[3],
        'HOST': dbparams[4],
        'PORT': dbparams[5],
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/geographyquiz/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)
