import datetime
import os
from os.path import join, dirname


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'long_SECRET_KEY'
    DEBUG = True
    DATABASE = '/tmp/site.db'
    UPLOAD_FOLDER = join(dirname(__file__), 'app_site/static/uploads')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'gif', 'png'}
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=60)
