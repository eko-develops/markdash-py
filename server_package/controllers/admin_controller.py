from server_package import db
from server_package.models.promotion import Promotion
from server_package.utils import Utils


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

    @staticmethod
    def create_data():
        dummy_data = [
            {
                "title": "10% off your first purchase",
                "description": "Get 10% off your first purchase when you sign up for our newsletter!",
                "start_date": "2023-01-01",
                "end_date": "2023-01-31",
                "user_id": 1,
            },
            {
                "title": "Free shipping on orders over $50",
                "description": "Spend over $50 and get free shipping on your order!",
                "start_date": "2023-02-01",
                "end_date": "2023-02-28",
                "user_id": 1,
            },
            {
                "title": "Buy one, get one 50% off",
                "description": "Buy one item at full price and get the second item of equal or lesser value at 50% off!",
                "start_date": "2023-03-01",
                "end_date": "2023-03-31",
                "user_id": 1,
            },
            {
                "title": "20% off all items",
                "description": "Get 20% off all items in our store!",
                "start_date": "2023-04-01",
                "end_date": "2023-04-30",
                "user_id": 1,
            },
            {
                "title": "Free gift with purchase",
                "description": "Spend over $100 and receive a free gift with your purchase!",
                "start_date": "2023-05-01",
                "end_date": "2023-05-31",
                "user_id": 1,
            },
        ]

        for data in dummy_data:
            data["start_date"] = Utils.convertToUTC(data["start_date"])
            data["end_date"] = Utils.convertToUTC(data["end_date"])

            promotion = Promotion(
                title=data["title"],
                description=data["description"],
                start_date=data["start_date"],
                end_date=data["end_date"],
                user_id=data["user_id"],
            )
            db.session.add(promotion)

        db.session.commit()

        return True
