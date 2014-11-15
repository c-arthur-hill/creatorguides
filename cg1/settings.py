"""
Django settings for cg1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from S3 import CallingFormat
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def bool_env(val):
    """Replaces string based environment values with Python booleans"""
    return True if os.environ.get(val, False) == "True" else False

SECRET_DJANGO_KEY = os.environ.get("SECRET_DJANGO_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCES_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_CALLING_FORMAT = os.environ.get("AWS_CALLING_FORMAT")
S3_STORAGE = os.environ.get("S3_STORAGE")
SITE_URL = 'http://sciguides.com/'
STATICFILES_STORAGE = S3_STORAGE
DEFAULT_FILE_STORAGE = S3_STORAGE
DEBUG = bool_env("DEBUG")
STATIC_URL = 'https://s3-us-west-2.amazonaws.com/creatorguides/'
LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/guides/"
AUTH_USER_MODEL = 'auth.user'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "cg1.context_processors.site_url",
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_DJANGO_KEY

# SECURITY WARNING: don't run with debug turned on in production!

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    "creatorguides.com",
    "sciguides.com"
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'groupings',
    'theories',
    'guides',
    'storages',
    'statics',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cg1.urls'

WSGI_APPLICATION = 'cg1.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.  '
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
