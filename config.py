import datetime
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'long_SECRET_KEY'
    DEBUG = True
    DATABASE = '/tmp/site.db'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=60)
