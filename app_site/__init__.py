from flask import Flask
from config import Config

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
# app.config['SECRET_KEY'] = 'long_SECRET_KEY'


from app_site import routes
