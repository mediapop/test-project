# Django settings for perfsystems project.
import os, logging, sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

path_to_mplib = os.path.join(os.path.dirname(__file__), '../../../')

sys.path.append(path_to_mplib)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'perfs',                      # Or path to database file if using sqlite3.
        'USER': 'perfs',                      # Not used with sqlite3.
        'PASSWORD': 'perfs',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Etc/GMT'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'
CDN_URL = None

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n8%5*eou)ol%aod@q&xm=!a0b0sh%tgy=rqls039f8=sk6echp'

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
    'django.contrib.messages.middleware.MessageMiddleware',
    'mplib.middleware.IgnoreFbCsrfMiddleware',

)


TEMPLATE_CONTEXT_PROCESSORS = (
    'mplib.context_processors.media_url', 
    'mplib.context_processors.facebook_settings', 
    'mplib.context_processors.facebook_client_settings',     
    'django.contrib.messages.context_processors.messages', 
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    'django.core.context_processors.csrf',
)


ROOT_URLCONF = 'perfsystems.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates'),

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    'django.contrib.humanize',
    
    # sentry is an error logger
    'indexer',
    'paging',
    'sentry',
    'sentry.client',
    'debug_toolbar',
    
    'django_ses',
    'django.contrib.markup',
    'paypal.standard.pdt', 
    
    'mplib',
    
    
    'fb_test',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

DATABASE_ROUTERS = ['mplib.db_routers.SentryRouter', 'mplib.db_routers.CommonRouter', ]

LOGGING_LEVEL = logging.INFO

FACEBOOK_APP_SECRET = ''
FACEBOOK_APP_URL = ''
FACEBOOK_APP_ID = ''
FACEBOOK_APP_KEY = ''

FACEBOOK_APPS = {}

ENVIRONMENT = 'dev'
DOMAIN_NAME = '127.0.0.1:8000'


# we need this for IE / FB in order to make cookies stick
P3P_COMPACT = 'policyref="http://dev.mediapop.info/p3p.xml", CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
MIDDLEWARE_CLASSES += ('mplib.middleware.P3PHeaderMiddleware',)
AUTHENTICATION_BACKENDS = ('mplib.backend.FacebookBackend',
                           'django.contrib.auth.backends.ModelBackend', )

PAYPAL_RECEIVER_EMAIL = 'payments@cannla.com'
PAYPAL_IDENTITY_TOKEN = None
