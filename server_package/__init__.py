"""Initialize application"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""Creating a Flask app, setting the database location, create db object"""
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

import server_package.routes.user_routes
import server_package.routes.admin_routes
import server_package.routes.promotion_routes
