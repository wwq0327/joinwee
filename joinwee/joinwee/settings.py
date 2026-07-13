# -*- coding: utf-8 -*-
# Django settings for joinwee project.
import os
import socket

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

if socket.gethostname() != 'AY131023174608652af9Z':
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
        ('master', 'master@joinwee.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wee',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'gogo90',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.joinwee.com', '115.29.168.222']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Chongqing'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = path('../media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = path('../static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    path('../static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&bo3e3!)z=iqe61hn!zh@u(*(o4c=p*@0e6q#dl6u5gr7+if(#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'linaro_django_pagination.middleware.PaginationMiddleware'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'joinwee.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'joinwee.wsgi.application'

TEMPLATE_DIRS = (
        path('../templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django.contrib.comments',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'userena',
    'userena.contrib.umessages',
    'guardian',
    'easy_thumbnails',
    # 'pagedown',
    # 'epiceditor',
    # 'taggit',
    'linaro_django_pagination',
    'bootstrap3',
    'hitcount',
    'notifications',
    'social_auth',
    #self
    'home',
    'profiles',
    #'brands',
    'abugs',
    'weelesson',
    'weemeet',
    'study',
    'topics',
    'fav',
#   'tags',
    'blog',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# login
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
LOGIN_REDIRECT_URL = '/'
USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
AUTH_PROFILE_MODULE = 'profiles.Profile'

# 禁止注册
#USERENA_DISABLE_SIGNUP = True

#USERENA_DISABLE_PROFILE_LIST = True
USERNAME_WITHOUT_USERNAMES = True
USERENA_MUGSHOT_SIZE = 140
USERENA_LANGUAGE_FIELD = 'zh-cn' # userena 语言设置
USERENA_DEFAULT_PRIVACY = 'open' #open所有人，registered仅注册用户,closed仅自己
ANONYMOUS_USER_ID = -1
ACCOUNT_ACTIVATION_DAYS = 7
#USERENA_ACTIVATION_REQUIRED=False
# email
#BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@joinwee.com' #'postmaster@sll.mailgun.org'
EMAIL_HOST = 'smtp.exmail.qq.com' #'smtp.mailgun.org'
#EMAIL_PORT = '993'
EMAIL_HOST_USER = 'noreply@joinwee.com' #'postmaster@sll.mailgun.org'
EMAIL_HOST_PASSWORD = 'c26c4dd5a6b61'

#page
PAGINATION_DEFAULT_PAGINATION = 3

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    'social_auth.context_processors.social_auth_by_type_backends',
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'social_auth.backends.contrib.douban.DoubanBackend2',
    'social_auth.backends.contrib.weibo.WeiboBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#pic
MAX_IMAGE_SIZE = 1024 * 700
MAX_UPLOAD_SIZE = 1024 * 1024 * 50

THUMBNAIL_ALIASES = {
        '': {
            'lesson': {'size': (253, 168), 'crop': True}, #用于lesson列表图片
            'avatar': {'size': (300, 200), 'crop': True}, #lesson展示页面图片
            'weex': {'size': (300, 120), 'crop': True}, #品牌图片
            'header': {'size': (160, 160), 'crop': True}, #lesson展示页面的头像
            'com_header': {'size': (64, 64), 'crop': True}, #讨论留言个人头像
            },
        }


#hitcount
HITCOUNT_KEEP_HIT_ACTIVE = { 'days': 7 }
HITCOUNT_HITS_PER_IP_LIMIT = 0
HITCOUNT_EXCLUDE_USER_GROUP = ( 'Editor', )

if socket.gethostname() == 'AY131023174608652af9Z':
    #social auth config
    ## douban oauth2
    DOUBAN2_CONSUMER_KEY = '0fc0b9908b9cd40d2f422cb1a2d67c27'
    DOUBAN2_CONSUMER_SECRET = 'edde6b053f96a59c'

    ## weibo oauth2
    WEIBO_CLIENT_KEY = '3185370992'
    WEIBO_CLIENT_SECRET = '6be046d7fc809140ecc55d9b542da8b5'
else:
    
    #social auth config
    ## douban oauth2
    DOUBAN2_CONSUMER_KEY = '030951b0e4c9d91b091bf512ae5d8b51'
    DOUBAN2_CONSUMER_SECRET = '39fac0990286d3c9'

    ## weibo oauth2
    WEIBO_CLIENT_KEY = '131808974'
    WEIBO_CLIENT_SECRET = '23b22c057d2ac55d70907b49e18284a3'

    
## 避免登入後轉向網址與userena不合, 可加入設定
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/oauth/sns-redirect/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/oauth/new-social-user/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/oauth/sns-link/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/oauth/sns-link/'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    #'social_auth.backends.pipeline.misc.save_status_to_session',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'profiles.pipeline.create_profile', # 自己在accounts這個app下建的pipeline.py
    'profiles.pipeline.set_guardian_permissions', # 自己在accounts這個app下建的pipeline.py
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    )


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
        # 'console': {
        #     'level':'DEBUG',
        #     'class': 'logging.StreamHandler',
        # },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'propagate': True,
        #     'level': 'DEBUG',
        # },
    }
}
