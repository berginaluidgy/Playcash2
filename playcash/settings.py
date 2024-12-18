"""
Django settings for playcash project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# from psycopg2._psycopg import BINARY, NUMBER, STRING, DATETIME, ROWID
from pathlib import Path
DROPBOX_ACCESS_TOKEN = 'sl.CAdEqWaJ8Vo52agStmp1URbKlaaHDW5Kw3PFyS76MMNUj3nXUrwHVYPCMH4tgfRkUjDlJVaDgWoo5YR7LiZPRT0ckwYy3A_pwkjp3RWSI15SOwWa86P95GWYYaIH9_usxwOYNE_UHM_BKe8oe6z0Eeg'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i^5%d%6j=$i&yta9m&bbfhjo@s0a1l7gm!al0yi_4%@qre*9t&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
      
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  
    'rest_framework_simplejwt',
    'playapp',
    'corsheaders',
    
]

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

ROOT_URLCONF = 'playcash.urls'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.UserRateThrottle',  # Pour les utilisateurs authentifiés
    #     'rest_framework.throttling.AnonRateThrottle',  # Pour les utilisateurs non authentifiés
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'user': '5/minute',  # 5 requêtes par minute pour les utilisateurs authentifiés
    #     'anon': '1/minute',  # 2 requêtes par minute pour les utilisateurs non authentifiés
    #     'custom': '10/hour',  # Exemple d'une limite personnalisée
    # }
}
# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:5173",  # Origine du frontend
#     "http://127.0.0.1:5173",  # Si le frontend utilise 127.0.0.1
# ]

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",
# ]

# # Si vous utilisez des cookies pour l'authentification :
# CORS_ALLOW_CREDENTIALS = True
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

WSGI_APPLICATION = 'playcash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'playcashbd',  # Nom de la base
        'USER': 'playcashbd_user',
        'PASSWORD': 'sZFuF9wcXiyRm5hLRQ7utudijOULbMFx',
        'HOST': 'dpg-ctd2ojt2ng1s73fturu0-a.oregon-postgres.render.com',
        'PORT': '5432',
        

    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True
