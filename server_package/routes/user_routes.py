from flask import request

from server_package import app
from server_package.controllers.user_controller import UserController as UC


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
