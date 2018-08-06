"""
Django settings for niproyecciones project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import redis

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = [('Julio Brito', 'jucebridu@gmail.com')]

ALLOWED_HOSTS = [
    os.getenv('ALLOWED_HOSTS_1'),
    os.getenv('ALLOWED_HOSTS_2'),
    os.getenv('ALLOWED_HOSTS_3'),
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ni proyecciones
    'users.apps.UsersConfig',
    'dashboard.apps.DashboardConfig',
    'tareas.apps.TareasConfig',
    'consultas.apps.ConsultasConfig',
    'estaciones.apps.EstacionesConfig',
    'partes.apps.PartesConfig',
    'proyecciones.apps.ProyeccionesConfig',
    'hw_proyecciones.apps.HwProyeccionesConfig',
    'hw_actividades.apps.HwActividadesConfig',
    'consumos.apps.ConsumosConfig',
    'llegadas.apps.LlegadasConfig',
    'existencias.apps.ExistenciasConfig',
    'resultados.apps.ResultadosConfig',
    'impactos.apps.ImpactosConfig',
    'formatos.apps.FormatosConfig',
    'rastreos.apps.RastreosConfig',
    'asignaciones.apps.AsignacionesConfig',
    # thirds
    'crispy_forms',
    'import_export',
    'storages',
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

ROOT_URLCONF = 'niproyecciones.urls'

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

WSGI_APPLICATION = 'niproyecciones.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

class NokiaGiRouter(object):

    def db_for_read(model, **hints):
        if model._meta.app_label == 'hw_proyecciones':
            return 'nokiagi_db'
        return None

    def db_for_write(model, **hints):
        if model._meta.app_label == 'hw_proyecciones':
            return 'nokiagi_db'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     if obj1._meta.app_label == 'hw_proyecciones' or \
    #        obj2._meta.app_label == 'proyecciones':
    #        return True
    #     return None

DATABASE_ROUTERS = [ NokiaGiRouter, ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': '5432',
        'HOST': os.getenv('DB_HOST'),
    },
    'nokiagi_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NOKIAGI_DB_NAME'),
        'USER': os.getenv('NOKIAGI_DB_USERNAME'),
        'PASSWORD': os.getenv('NOKIAGI_DB_PASSWORD'),
        'PORT': '3306',
        'HOST': os.getenv('NOKIAGI_DB_HOST'),
        'OPTIONS': {
            'sql_mode':'STRICT_TRANS_TABLES',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = os.getenv('STATIC_URL')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = os.getenv('MEDIA_URL')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_PROFILE_MODULE = 'users.Perfil'

GS_BUCKET_NAME = os.getenv('BUCKET_NAME')

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

IMPORT_EXPORT_USE_TRANSACTIONS = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

DATA_UPLOAD_MAX_MEMORY_SIZE = None

VIERNES = 4

SABADO = 5

DOMINGO = 6

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_REDIRECT_EXEMPT = ['create/hw/estacion/',
                          'update/hw/estacion/',
                          'delete/hw/estacion/',
                          'delete/hw/proyeccion/',
                          'create/hw/proyeccion/',
                          'update/hw/proyeccion/',
                          'update/hw/actividad/',
                          'calculate/consumo/nokia/',
                          'delete/impacto/',
                          'create/impacto/',
                          'calculate/impacto/',
                          'calculate/tipo/impacto/',
                          'create/proyeccion/estacion/entro/',
                          'create/proyeccion/estacion/salio/',
                          'send/mail/proyeccion/',
                         ]

EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

CELERY_BROKER_URL = os.getenv('REDIS_URL')
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

REDIS = redis.StrictRedis(host=os.getenv('REDIS_HOST'), port=6379, db=0)

try:
    from local_settings import *
except ImportError:
    pass
