import datetime
import os
# from os.path import join, dirname, realpath


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'long_SECRET_KEY'
    DEBUG = True
    DATABASE = '/tmp/site.db'
    UPLOAD_FOLDER = '/static/uploads'
    # UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads/..')
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'gif', 'png'])
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=60)
