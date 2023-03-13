"""Initialize application"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

"""Creating a Flask app, setting the database location, create db object"""
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import server_package.routes.user_routes
import server_package.routes.admin_routes
import server_package.routes.promotion_routes
