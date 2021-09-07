from ._base import *

DEBUG = True

SECRET_KEY="Super"

# WEBSITE_URL = "http://127.0.0.1:8000"
WEBSITE_URL = ''
if os.getenv('HOST_IP'):
    ALLOWED_HOSTS.append(os.getenv('HOST_IP'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    },
}