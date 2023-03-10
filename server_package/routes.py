"""Module for handling routes with controllers."""

from flask import request

from server_package import app
from server_package.controllers.admin_controller import AdminController as AC
from server_package.controllers.user_controller import UserController as UC
from server_package.controllers.promotion_controller import PromotionController as PC


# Dummy Data
dummy_promotions = [
    {"name": "Weekly Wednesday", "description": "10% off every Wednesday, every week"},
    {"name": "Sunday Funday", "description": "20% off all items"},
]


@app.get("/promotions")
def promotion_list():
    promotions = PC.get_all_promotions()
    return {"promotions": promotions}


@app.post("/promotion")
def create_promotion():
    promotion_data = request.get_json()
    promotion = PC.create_promotion(promotion_data)

    return {"new_promotion": promotion}


@app.get("/users")
def user_list():
    """Returns a list of dictionaries representing all the users."""
    users = UC.get_all_users()
    return {"users": users}


@app.get("/user/<int:user_id>")
def user_get(user_id):
    """Returns a single user."""
    user = UC.get_user_by_id(user_id)

    if user:
        return {"user": user}
    return {"user": {}, "message": f"No user found with ID {user_id}."}, 409


@app.post("/user")
def user_post():
    """Adds a new user and returns the new user."""
    new_user_data = request.get_json()

    new_user = UC.create_user(new_user_data)

    response = {"new_user": {}}
    if new_user == -1:
        response["message"] = "Username already exists."
        return response, 409
    if new_user == -2:
        response["message"] = "Email already exists."
        return response, 409

    response["message"] = "New user created."
    return {"new_user": new_user}, 201


@app.delete("/delete/all")
def delete_all():
    """Deletes all tables in the database"""
    AC.drop_all()
    return {"message": "Deleted all tables in database"}


@app.post("/create/tables")
def create_tables():
    """Create tables from Models"""
    AC.create_tables()
    return {"message": "Created User and Promotions tables"}
