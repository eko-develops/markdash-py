from flask import request

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
