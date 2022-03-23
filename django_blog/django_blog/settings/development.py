from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*", "3.127.243.35", "raphaela.lundinfo.com"]

STATIC_ROOT = "/home/ubuntu/static"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "raphiie", # "djangodb" or "raphiie"
        "USER": "raphiie",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
        # "listen_addresses": "0.0.0.0",
    }
}

SECRET_KEY = "django-insecure-#)s89bg&=!ge!eb_wh+h_8+-*fj9*ay=)gfjf70r@g#@($f!h7"
