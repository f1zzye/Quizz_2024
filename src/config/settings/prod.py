from django.conf.global_settings import STATIC_ROOT

from config.settings.base import *  # noqa

DEBUG = True

SECRET_KEY = "django-secret-key"

ALLOWED_HOSTS = ["localhost"]

STATIC_ROOT = BASE_DIR.parent / "static/"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR.parent / "media/"
MEDIA_URL = "/media/"

DATABASES = {
    # "default_local": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "my_database",
    #     "USER": "userdb",
    #     "PASSWORD": "admin",
    #     "HOST": "localhost",
    #     "PORT": 5432,
    # },
    # "default_sql": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # },
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    },
}
