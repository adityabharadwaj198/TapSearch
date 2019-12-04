from flask import Flask
from app.createindex import Database, InvertedIndex
import os
app= Flask(__name__)
app.config['SECRET_KEY'] = 'youwontguess'
basedir = os.path.abspath(os.path.dirname(__file__))
app.static_folder = 'static'

from app.routes import app_blueprint
app.register_blueprint(app_blueprint)