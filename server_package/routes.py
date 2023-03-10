from flask import jsonify

from server_package.models import User
from server_package import app, db


"""Dummy data"""
promotions = [
    {"name": "Weekly Wednesday", "description": "10% off every Wednesday, every week"},
    {"name": "Sunday Funday", "description": "20% off all items"},
]


@app.route("/users")
def user_list():
    """Returns a list of dictionaries representing a user"""
    query = db.select(User).order_by(User.id)
    users = db.session.execute(query).scalars()

    user_res_list = []

    for user in users:
        user_res_list.append(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "image_file": user.image_file,
                "password": user.password,
            }
        )
    return jsonify({"users": user_res_list})


@app.route("/delete/all")
def delete_all():
    """Deletes all tables in the database"""
    db.drop_all()
    return jsonify({"message": "Deleted all tables in database"})


@app.route("/create/tables")
def create_tables():
    """Create tables from Models"""
    db.create_all()
    return jsonify({"message": "Created User and Promotions tables"})
