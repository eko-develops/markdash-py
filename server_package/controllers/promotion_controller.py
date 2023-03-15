from datetime import datetime, timezone

from server_package import db
from server_package.models.promotion import Promotion


class PromotionController:
    """Controller for handling the Promotion model."""

    @staticmethod
    def get_all_promotions():
        """Returns a list of all the Users."""
        query = db.select(Promotion).order_by(Promotion.title)
        promotions = db.session.execute(query).scalars()

        promotions_list = []

        for promotion in promotions:
            promotions_list.append(
                {
                    "id": promotion.id,
                    "title": promotion.title,
                    "description": promotion.description,
                    "date_posted": promotion.date_posted,
                    "start_date": promotion.start_date,
                    "end_date": promotion.end_date,
                    "scheduled": promotion.scheduled,
                    "author": {
                        "id": promotion.author.id,
                        "username": promotion.author.username,
                        "email": promotion.author.email,
                    },
                }
            )
        return promotions_list

    @staticmethod
    def create_promotion(new_promotion):
        """Returns a list of all the Users."""
        promo_title = new_promotion["title"]
        promo_description = new_promotion["description"]
        promo_author = new_promotion["user_id"]
        promo_start_date = new_promotion["start_date"]
        promo_end_date = new_promotion["end_date"]

        if promo_start_date:
            promo_start_date = datetime.fromisoformat(promo_start_date).replace(
                tzinfo=timezone.utc
            )
        else:
            promo_start_date = None

        if promo_end_date:
            promo_end_date = datetime.fromisoformat(promo_end_date).replace(
                tzinfo=timezone.utc
            )
        else:
            promo_end_date = None

        promotion = Promotion(
            title=promo_title,
            description=promo_description,
            user_id=promo_author,
            start_date=promo_start_date,
            end_date=promo_end_date,
        )

        db.session.add(promotion)
        db.session.commit()

        return {
            "id": promotion.id,
            "title": promotion.title,
            "description": promotion.description,
            "start_date": promo_start_date,
            "end_date": promo_end_date,
            "date_posted": promotion.date_posted,
            "scheduled": promotion.scheduled,
        }

    @staticmethod
    def delete_promo(data):
        promo_id = data["promotion_id"]

        query = db.select(Promotion).where(Promotion.id == promo_id)
        promotion = db.session.execute(query).scalar()

        deleted_promotion = {
            "id": promotion.id,
            "title": promotion.title,
            "description": promotion.description,
            "date_posted": promotion.date_posted,
            "start_date": promotion.start_date,
            "end_date": promotion.end_date,
            "scheduled": promotion.scheduled,
        }

        db.session.delete(promotion)
        db.session.commit()

        return deleted_promotion

    @staticmethod
    def set_scheduled(data):
        promo_id = data["id"]

        query = db.select(Promotion).where(Promotion.id == promo_id)
        promotion = db.session.execute(query).scalar()

        if promotion.scheduled:
            promotion.scheduled = False
        else:
            promotion.scheduled = True

        db.session.commit()

        return {
            "id": promotion.id,
            "title": promotion.title,
            "description": promotion.description,
            "date_posted": promotion.date_posted,
            "start_date": promotion.start_date,
            "end_date": promotion.end_date,
            "scheduled": promotion.scheduled,
        }
