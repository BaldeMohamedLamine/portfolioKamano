from __future__ import annotations

from .settings import *
import dj_database_url 
import environ
import os
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


SECRET_KEY = env('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
DATABASES = {'defalt': dj_database_url.config(conn_health_checks=True)}
