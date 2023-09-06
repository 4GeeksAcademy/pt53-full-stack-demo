from enum import Enum
from uuid import uuid4
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import (
    generate_password_hash, check_password_hash
)

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(
        db.String(256),
        unique=False,
        nullable=False,
        default="CHANGE THIS PASSWORD"
    )
    is_active = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "pets": [pet.serialize() for pet in self.pets],
        }

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)


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


# Space Ghost:
post_to_post = db.Table(
    "post_to_post",
    db.metadata,
    db.Column(
        "parent_post_id",
        db.Integer,
        db.ForeignKey('post.id')
    ),
    db.Column(
        "child_post_id",
        db.Integer,
        db.ForeignKey('post.id')
    ),
)


class Post(db.Model):
    """
        This type of structure (a tree) could be used for:
            - ecommerce (category trees)
            - Media libraries (content organization)
            - Folder structures (folders)
            - HTML documents
    """
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(
        "User",
        backref=db.backref(
            "posts",
            uselist=True
        ),
        uselist=False
    )
    parent = db.relationship(
        "Post",
        secondary=post_to_post,
        primaryjoin=(id == post_to_post.c.parent_post_id),
        secondaryjoin=(id == post_to_post.c.child_post_id),
        backref=db.backref(
            "replies",
            uselist=True
        ),
        uselist=False
    )

    def __repr__(self):
        return f"<Post {self.title}>"

    def serialize(self, children=True):
        data = {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author.serialize(),
            "parent": None if not self.parent else self.parent.id,
        }

        if children:
            return {
                **data,
                "replies": [reply.serialize() for reply in self.replies],
            }
        return data


category_tree = db.Table(
    "category_tree",
    db.metadata,
    db.Column(
        "parent_cat_id",
        db.Integer,
        db.ForeignKey('category.id')
    ),
    db.Column(
        "child_cat_id",
        db.Integer,
        db.ForeignKey('category.id')
    ),
)


cat_to_prod = db.Table(
    "cat_to_prod",
    db.metadata,
    db.Column(
        "category_id",
        db.Integer,
        db.ForeignKey('category.id')
    ),
    db.Column(
        "product_id",
        db.Integer,
        db.ForeignKey('product.id')
    ),
)


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    parent = db.relationship(
        "Category",
        secondary=category_tree,
        primaryjoin=(id == category_tree.c.parent_cat_id),
        secondaryjoin=(id == category_tree.c.child_cat_id),
        backref=db.backref(
            "children",
            uselist=True
        ),
        uselist=False
    )

    def __repr__(self):
        return f"<Category {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "parent": None if not self.parent else self.parent.id,
            "children": [
                child.serialize() for child in self.children
            ]
        }


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    description = db.Column(db.Text())
    price = db.Column(db.Float())  # Don't use floats for money, please.
    cost = db.Column(db.Float())  # Don't use floats for money, please.
    categories = db.relationship(
        "Category",
        secondary=cat_to_prod,
        primaryjoin=(id == cat_to_prod.c.product_id),
        backref=db.backref(
            "products",
            uselist=True
        ),
        uselist=True
    )

    def __repr__(self):
        return f"<Product {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "cost": self.cost,
            "categories": [
                cat.name for cat in self.categories
            ],
        }


class StoredData(db.Model):
    __tablename__ = "stored_data"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(128), unique=True)
    value = db.Column(db.JSON)

    def __repr__(self):
        return f"<Product {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "key": self.key,
            "value": self.value,
        }


class PasswordReset(db.Model):
    __tablename__ = "pass_reset"
    id = db.Column(db.Integer, primary_key=True)

    reset_id = db.Column(db.String(36), default=uuid4, unique=True)
    created = db.Column(db.DateTime, default=datetime.now)
    complete = db.Column(db.DateTime, default=None)
    email_sent = db.Column(db.DateTime, default=None)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(
        "User", uselist=False
    )
