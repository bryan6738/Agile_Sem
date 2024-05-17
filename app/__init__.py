from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config
from flask_mde import Mde
from flask_moment import Moment
# from .routes import *


app = Flask(__name__)
mde = Mde(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

login = LoginManager(app)
login.login_view = 'login'

# from . import routes, models
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import test_data

# file: __init__.py



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Update your configuration appropriately
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables for our data models
    
    return app

