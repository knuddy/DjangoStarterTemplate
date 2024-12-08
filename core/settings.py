import os
from pathlib import Path
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", default='foo')
DEBUG = int(os.environ.get("DEBUG", default=True))
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", default='*').split(" ")
CSRF_TRUSTED_ORIGINS = [os.environ.get("CSRF_TRUSTED_ORIGINS", default='http://localhost')]
SSL_VERIFY = int(os.environ.get("SSL_VERIFY", default=0))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

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

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE_DEFAULT', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DB_NAME_DEFAULT', 'postgres'),
        'USER': os.environ.get("DB_USER_DEFAULT", 'postgres'),
        'PASSWORD': os.environ.get("DB_PASSWORD_DEFAULT", 'postgres'),
        "HOST": os.environ.get("DB_HOST_DEFAULT", 'localhost'),
        "PORT": os.environ.get("DB_PORT_DEFAULT", '1396'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "core.cache.RedisCache",
        "LOCATION": os.environ.get('CACHE_LOCATION_DEFAULT', 'redis://localhost:6379/0'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = os.environ.get("STATIC_URL", default='/staticfiles/')
STATIC_ROOT = os.path.join(BASE_DIR, os.environ.get("STATIC_ROOT", default='staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

MEDIA_URL = os.environ.get("MEDIA_URL", default='/mediafiles/')
MEDIA_ROOT = os.path.join(BASE_DIR, os.environ.get("MEDIA_ROOT", default='mediafiles'))

CELERY_TIMEZONE = 'Pacific/Auckland'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'redis://localhost:6379/15')
