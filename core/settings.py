from pathlib import Path
import os
from decouple import config
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent
IS_BUILD_PHASE = config('IS_BUILD_PHASE', default=False, cast=bool)

if not IS_BUILD_PHASE:
    ENVIRONMENT = config('ENVIRONMENT', default='development')
    CALLMEBOT_URL = config('CALLMEBOT_URL')
    CALLMEBOT_API_KEY = config('CALLMEBOT_API_KEY')
    CALLMEBOT_PHONE_NUMBER = config('CALLMEBOT_PHONE_NUMBER')
    if ENVIRONMENT == 'production':
        SECRET_KEY = config('SECRET_KEY')
        DEBUG = False
        ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')
    else:
        SECRET_KEY = config('SECRET_KEY', default='django-insecure-local-dev-key-!@#$%^&*()')
        DEBUG = True
        ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "students",
    "widget_tweaks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

LOGIN_URL = '/'

LOGIN_REDIRECT_URL = '/students/list/'

LOGOUT_REDIRECT_URL = '/'

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


if not IS_BUILD_PHASE:
    if ENVIRONMENT == 'production':
        DATABASES = {
            'default': dj_database_url.config(conn_max_age=600)
        }
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql_psycopg2",
                "NAME": config('POSTGRES_DB'),
                "USER": config('POSTGRES_USER'),
                "PASSWORD": config('POSTGRES_PASSWORD'),
                "HOST": config('POSTGRES_HOST'),
                "PORT": config('POSTGRES_PORT', cast=int),
            }
        }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "pt-BR"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
