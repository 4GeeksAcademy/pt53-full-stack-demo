from enum import Enum

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "pets": [pet.serialize() for pet in self.pets],
        }


class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(256))
    picture_url = db.Column(db.String(256))

    user = db.relationship(
        "User", uselist=False,
        backref=db.backref("pets", uselist=True)
    )

    def __repr__(self):
        return f'<Pet {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "picture_url": self.picture_url,
            "ratings": [rating.serialize() for rating in self.ratings],
        }


class Goodness(Enum):
    honest_to = -2
    thank = -1
    gracious = 0
    knows = 1
    sake = 2


class Rating(db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cuteness = db.Column(db.Integer, default=5)
    precociousness = db.Column(db.Integer, default=5)
    goodness = db.Column(db.Enum(Goodness), default=5)

    pet = db.relationship(
        "Pet", uselist=False,
        backref=db.backref("ratings", uselist=True)
    )
    user = db.relationship(
        "User", uselist=False,
        backref=db.backref("ratings", uselist=True)
    )

    def __repr__(self):
        return f'<Rating {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "pet_id": self.pet_id,
            "cuteness": self.cuteness,
            "precociousness": self.precociousness,
            "goodness": self.goodness.name,
            "good_value": self.goodness.value,
        }
