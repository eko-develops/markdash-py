"""Initialize application"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""Creating a Flask app, setting the database location, create db object"""
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

from server_package import routes
