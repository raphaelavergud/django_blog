from .base import *

DEBUG = False
ALLOWED_HOSTS = ["raphaelavergud.pythonanywhere.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "djangodb",
        "USER": "raphiie",
        "PASSWORD": "password",
        "HOST": "*",
        "PORT": "5432",
        # "listen_addresses": "0.0.0.0",
    }
}

SECRET_KEY = ""