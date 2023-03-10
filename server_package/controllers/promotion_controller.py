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
                    "author": promotion.user_id,
                }
            )
        return promotions_list

    @staticmethod
    def create_promotion(new_promotion):
        """Returns a list of all the Users."""
        promo_title = new_promotion["title"]
        promo_description = new_promotion["description"]
        promo_author = new_promotion["user_id"]

        promotion = Promotion(
            title=promo_title, description=promo_description, user_id=promo_author
        )

        db.session.add(promotion)
        db.session.commit()

        return {
            "id": promotion.id,
            "title": promotion.title,
            "description": promotion.description,
        }
