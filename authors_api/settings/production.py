from .base import *  # noqa
from .base import env

# TODO add domain names of the production server
CSRF_TRUSTED_ORIGINS = []

DATABASES = {"default": env.db("DATABASE_URL")}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SITE_NAME = "Authors Haven"