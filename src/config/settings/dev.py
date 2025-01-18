import os

import mongoengine

from config.settings.base import *  # noqa

DEBUG = True

SECRET_KEY = "django-secret-key"

ALLOWED_HOSTS = []

mongoengine.connect(
    host="mongodb://admin:admin@mongodb:27017/mongodb_content?authSource=admin",
)

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": 5432,
        },
    }
else:
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
