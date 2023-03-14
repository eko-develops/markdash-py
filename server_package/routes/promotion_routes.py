from flask import request, jsonify

from server_package import app
from server_package.controllers.promotion_controller import PromotionController as PC


@app.get("/promotions")
def promotion_list():
    promotions = PC.get_all_promotions()
    return {"promotions": promotions}


@app.post("/promotion")
def create_promotion():
    promotion_data = request.get_json()
    promotion = PC.create_promotion(promotion_data)

    return {"new_promotion": promotion}


@app.delete("/promotion")
def delete_promotion():
    """Delete a promotion by ID."""
    data = request.get_json()
    deleted_promo = PC.delete_promo(data)

    return {"deleted_promo": deleted_promo}


@app.post("/promotion/schedule")
def promotion_schedule():
    data = request.get_json()
    scheduled_promotion = PC.set_scheduled(data)

    return {"scheduled_promotion": scheduled_promotion}
