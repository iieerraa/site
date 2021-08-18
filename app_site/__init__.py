import os.path

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'site.db')))

from app_site import routes
