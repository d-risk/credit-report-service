"""
Django settings for credit_report_service project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import logging
import os
from logging import Logger
from typing import List, Dict, Any

from django.utils.crypto import get_random_string


def is_production() -> bool:
    """
    Always assume that code is running in production unless explicitly specified.
    :return: False if the code is to be executed in non-production mode, otherwise True.
    """
    return not bool(os.getenv('APP_PRODUCTION'))


def log_level() -> int:
    if is_production():
        return os.getenv('APP_LOG_LEVEL', logging.INFO)
    else:
        return logging.DEBUG


def secret_key() -> str:
    if is_production():
        key = os.getenv('APP_SECRET_KEY')
        if key is None or key == '':
            raise LookupError()
        return key
    else:
        return get_random_string(length=50)


logging.basicConfig(level=log_level())
logger: Logger = logging.getLogger(__name__)
if is_production():
    logger.setLevel(os.getenv('APP_LOG_LEVEL', 'INFO'))
else:
    logger.setLevel('DEBUG')
logger.info(f"APP_PRODUCTION={is_production()}")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: str = secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = not is_production()
logger.info(f"DEBUG={DEBUG}")

ALLOWED_HOSTS: List[str] = [
    '.d-risk.tech'
]
if DEBUG:
    ALLOWED_HOSTS += ['localhost', '127.0.0.1']
logger.info(f"ALLOWED_HOSTS={ALLOWED_HOSTS}")

# Application definition

INSTALLED_APPS: List[str] = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',

    # Graphene Django
    'graphene_django',
    'common',
    'company',
    'credit_report',
    'financial_report',
    'news',
    'credit_rating',
]

MIDDLEWARE: List[str] = [
    # 'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF: str = 'credit_report_service.urls'

TEMPLATES: List[Dict[str, Any]] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.debug',
                # 'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION: str = 'credit_report_service.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES: Dict[str, Dict[str, str]] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: List[Dict[str, str]] = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE: str = 'en-us'

TIME_ZONE: str = 'UTC'

USE_I18N: bool = True

USE_L10N: bool = True

USE_TZ: bool = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL: str = '/static/'

# Graphene
GRAPHENE: Dict[str, str] = {
    'SCHEMA': 'credit_report_service.schema.schema',
}
