from datetime import datetime

from server_package import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    promotions = db.relationship("Promotion", backref="author", lazy=True)

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email}, {self.image_file})"


class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Promotion({self.id}, {self.title}, {self.date_posted})"
