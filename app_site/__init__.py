from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'long_SECRET_KEY'


db = SQLAlchemy(app)


from app_site import routes
