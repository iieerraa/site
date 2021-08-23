import datetime
import os
from os.path import join, dirname


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'long_SECRET_KEY'  # Параметры кодирования
    DEBUG = True  # Дебаг
    DATABASE = '/tmp/site.db'  # путь к БД
    UPLOAD_FOLDER = join(dirname(__file__), 'app_site/static/img/uploads')  # Путь для созранения файлов
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'gif', 'png'}  # параметры принемаемых файлов
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=60)  # параметры длительности сессии
