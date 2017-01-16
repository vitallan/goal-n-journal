import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# url: /login/twitter

SOCIAL_AUTH_TWITTER_KEY = 'secret'
SOCIAL_AUTH_TWITTER_SECRET = 'secret'

# url: /login/google-oauth2/

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'secret'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'secret'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/new/'
SOCIAL_AUTH_LOGIN_URL = '/'
