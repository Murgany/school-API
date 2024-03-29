"""
Django settings for school_management_system project.
Generated by 'django-admin startproject' using Django 3.1.13.
"""

import os
import dotenv
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from .env file
load_dotenv()

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Secret key for Django project
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# Debug mode settings
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

# Test runner settings
TEST_RUNNER = 'django_heroku.HerokuDiscoverRunner'

# Allowed hosts for the project
ALLOWED_HOSTS = ['localhost']

# Installed applications for the project
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'knox',
]

# REST framework settings
REST_SESSION_LOGIN = True
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'knox.auth.TokenAuthentication',
    ),
    'DATETIME_FORMAT': "%d/%m/%y %H:%M:%S",
}

# CORS settings
CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
ACCESS_CONTROL_ALLOW_ORIGIN = ["http://localhost:3000"]

# Middleware settings
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration for the project
ROOT_URLCONF = 'schoolApi.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

# WSGI application configuration
WSGI_APPLICATION = 'schoolApi.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Load database settings from environment variables
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Load environment variables from .env file
dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Password validation settings
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
DATE_FORMAT = "%m/%d/%Y %H:%M:%S"
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = [
    ('en', 'English'),
    ('ar', 'Arabic'),
]

# Static files (CSS, JavaScript, Images) settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default auto field for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CSRF cookie settings
CSRF_COOKIE_SECURE = True

# Session cookie settings
SESSION_COOKIE_SECURE = True
