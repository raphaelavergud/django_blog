from .base import *

DEBUG = False
ALLOWED_HOSTS = ["raphaelavergud.pythonanywhere.com", "*", "3.127.243.35", "raphaela.lundinfo.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "raphiie",
        "USER": "raphiie",
        "PASSWORD": "password",
        "HOST": "*",
        "PORT": "5432",
        # "listen_addresses": "0.0.0.0",
    }
}

SECRET_KEY = ""