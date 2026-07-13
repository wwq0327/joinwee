# -*- coding: utf-8 -*-
import os
from decouple import config

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

ADMINS = (
    ('master', 'master@joinwee.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': config('DB_NAME', default=os.path.join(ROOT, '..', 'db.sqlite3')),
        'USER': config('DB_USER', default=''),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default=''),
        'PORT': config('DB_PORT', default=''),
    }
}

ALLOWED_HOSTS = ['.joinwee.com', '115.29.168.222', '127.0.0.1', 'localhost']

TIME_ZONE = 'Asia/Chongqing'

LANGUAGE_CODE = 'zh-hans'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = path('../media')

MEDIA_URL = '/media/'

STATIC_ROOT = path('../static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    path('../media'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = config('SECRET_KEY')

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
)

ROOT_URLCONF = 'joinwee.urls'

WSGI_APPLICATION = 'joinwee.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path('../templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'guardian',
    'easy_thumbnails',
    'bootstrap3',
    'hitcount',
    'notifications',
    #self
    'home',
    'profiles',
    'abugs',
    'weelesson',
    'weemeet',
    'study',
    'topics',
    'fav',
    'blog',
    'providers',
)

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 7

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@joinwee.com')
EMAIL_HOST = config('EMAIL_HOST', default='smtp.exmail.qq.com')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='noreply@joinwee.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# django-allauth settings
ACCOUNT_LOGIN_METHODS = {'username', 'email'}
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
ACCOUNT_SIGNUP_FORM_CLASS = 'profiles.forms.WeeSignupForm'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'douban': {
        'APP': {
            'client_id': config('DOUBAN_KEY', default=''),
            'secret': config('DOUBAN_SECRET', default=''),
        },
    },
    'weibo': {
        'APP': {
            'client_id': config('WEIBO_KEY', default=''),
            'secret': config('WEIBO_SECRET', default=''),
        },
    },
}
USE_HTTPS = False

#pic
MAX_IMAGE_SIZE = 1024 * 700
MAX_UPLOAD_SIZE = 1024 * 1024 * 50

THUMBNAIL_ALIASES = {
    '': {
        'lesson': {'size': (253, 168), 'crop': True},
        'avatar': {'size': (300, 200), 'crop': True},
        'weex': {'size': (300, 120), 'crop': True},
        'header': {'size': (160, 160), 'crop': True},
        'com_header': {'size': (64, 64), 'crop': True},
    },
}

#hitcount
HITCOUNT_KEEP_HIT_ACTIVE = { 'days': 7 }
HITCOUNT_HITS_PER_IP_LIMIT = 0
HITCOUNT_EXCLUDE_USER_GROUP = ( 'Editor', )


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Security settings (enable in production)
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=0, cast=int)
SECURE_CONTENT_TYPE_NOSNIFF = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
