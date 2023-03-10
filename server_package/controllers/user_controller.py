from server_package import db
from server_package.models.user import User


class UserController:
    """The controller used for handling the User model."""

    @staticmethod
    def get_all_users():
        """Returns a list of all the Users."""
        query = db.select(User).order_by(User.id)
        users = db.session.execute(query).scalars()

        user_list = []

        for user in users:
            user_info_dict = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "image_file": user.image_file,
                "password": user.password,
            }

            user_promotions = []
            for promotion in user.promotions:
                user_promotions.append(
                    {
                        "id": promotion.id,
                        "title": promotion.title,
                        "description": promotion.description,
                        "date_posted": promotion.date_posted,
                    }
                )

            user_info_dict["promotions"] = user_promotions
            user_list.append(user_info_dict)

        return user_list

    @staticmethod
    def get_user_by_id(user_id):
        """Returns a user by id."""
        query = db.select(User).where(User.id == user_id)
        user = db.session.execute(query).scalar()

        if user:
            user_info_dict = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "image_file": user.image_file,
            }

            user_promotions = []
            for promotion in user.promotions:
                user_promotions.append(
                    {
                        "id": promotion.id,
                        "title": promotion.title,
                        "description": promotion.description,
                        "date_posted": promotion.date_posted,
                    }
                )

            user_info_dict["promotions"] = user_promotions

            return user_info_dict

        return None

    @staticmethod
    def get_user_by_username(username):
        """Returns a user by their username."""
        query = db.select(User).where(User.username == username)
        user = db.session.execute(query).scalar()
        if user:
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "image_file": user.image_file,
            }
        return False

    @staticmethod
    def get_user_by_email(email):
        """Returns a user by their email."""
        query = db.select(User).where(User.email == email)
        user = db.session.execute(query).scalar()
        if user:
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "image_file": user.image_file,
            }
        return False

    @staticmethod
    def create_user(new_user_data):
        """Add a new user to the database then return the new user."""
        username = new_user_data["username"]
        if UserController.get_user_by_username(username):
            return -1

        email = new_user_data["email"]
        if UserController.get_user_by_email(email):
            return -2

        password = new_user_data["password"]

        new_user = User(username=username, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()

        return {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "image_file": new_user.image_file,
        }
