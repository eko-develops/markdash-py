from server_package import db


class AdminController:
    """The controller used for handling admin database operations. Development only."""

    @staticmethod
    def drop_all():
        """Drops all tables in the database."""
        db.drop_all()

    @staticmethod
    def create_tables():
        """Create tables based on models."""
        db.create_all()
