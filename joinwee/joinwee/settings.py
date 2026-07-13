# -*- coding: utf-8 -*-
import os
import socket

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

if socket.gethostname() != 'AY131023174608652af9Z':
    DEBUG = True
else:
    DEBUG = False

ADMINS = (
    ('master', 'master@joinwee.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wee',
        'USER': 'root',
        'PASSWORD': 'gogo90',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'charset': 'utf8',
        },
    }
}

ALLOWED_HOSTS = ['.joinwee.com', '115.29.168.222']

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

SECRET_KEY = '&bo3e3!)z=iqe61hn!zh@u(*(o4c=p*@0e6q#dl6u5gr7+if(#'

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
)

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 7

DEFAULT_FROM_EMAIL = 'noreply@joinwee.com'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_HOST_USER = 'noreply@joinwee.com'
EMAIL_HOST_PASSWORD = 'c26c4dd5a6b61'

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

if socket.gethostname() == 'AY131023174608652af9Z':
    # douban oauth2 - production
    DOUBAN2_CONSUMER_KEY = '0fc0b9908b9cd40d2f422cb1a2d67c27'
    DOUBAN2_CONSUMER_SECRET = 'edde6b053f96a59c'
    # weibo oauth2 - production
    WEIBO_CLIENT_KEY = '3185370992'
    WEIBO_CLIENT_SECRET = '6be046d7fc809140ecc55d9b542da8b5'
else:
    # douban oauth2 - dev
    DOUBAN2_CONSUMER_KEY = '030951b0e4c9d91b091bf512ae5d8b51'
    DOUBAN2_CONSUMER_SECRET = '39fac0990286d3c9'
    # weibo oauth2 - dev
    WEIBO_CLIENT_KEY = '131808974'
    WEIBO_CLIENT_SECRET = '23b22c057d2ac55d70907b49e18284a3'

# SOCIALACCOUNT_PROVIDERS = {
#     'douban': {
#         'APP': {
#             'client_id': DOUBAN2_CONSUMER_KEY,
#             'secret': DOUBAN2_CONSUMER_SECRET,
#             'key': '',
#         }
#     },
#     'weibo': {
#         'APP': {
#             'client_id': WEIBO_CLIENT_KEY,
#             'secret': WEIBO_CLIENT_SECRET,
#             'key': '',
#         }
#     },
# }

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

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
