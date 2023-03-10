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
