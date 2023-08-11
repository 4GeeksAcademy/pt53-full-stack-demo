"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import request, jsonify, Blueprint
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash

from api.models import db, User, Pet
from datetime import date

api = Blueprint('api', __name__)


@api.route("/jwt", methods=["GET"])
def what_even_is_a_jwt():
    """
    This demonstrates what a JWT token looks like,
    you should paste the token value into JWT.io and
    check it out.
    """
    token = create_access_token(
        "The argument you pass in here is the identity of the token."
    )
    return jsonify(
        token=token,
    )


@api.route("/jwt_ident", methods=["GET"])
@jwt_required()
def what_even_is_an_identity():
    ident = get_jwt_identity()
    return jsonify(
        identity=ident,
        user=User.query.filter_by(email=ident).first().serialize()
    )


@api.route('/pwd/<string:password>')
def pwd_hash(password):
    return generate_password_hash(password), 200


@api.route("/login", methods=["POST"])
def login():
    """
    Accepts application/json
    POST
    {
        "email": "sombra@catemail.com",
        "password": "LittleBlueParrotToy"
    }

    Returns:
    {
        "token": "some JWT token"
    }
    """
    data = request.json
    user = User.query.filter_by(email=data.get("email", None)).first()

    if not user:
        return jsonify(message="Invalid credentials"), 401
    if not user.check_password(data.get("password", None)):
        return jsonify(message="Invalid credentials"), 401

    token = create_access_token(user.email)
    return jsonify(token=token), 200


@api.route("/signup", methods=["POST"])
def signup():
    """
    Accepts application/json
    POST
    {
        "email": "sombra@catemail.com",
        "password": "LittleBlueParrotToy"
    }

    Returns: 204
    """
    data = request.json
    user = User.query.filter_by(email=data.get("email", None)).first()
    if user:
        return jsonify(message="A user with that email already exists!"), 400

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return '', 204


@api.route("/is_it_friday_yet", methods=["GET", "POST"])
def is_it_friday():
    if request.method == "POST":
        return jsonify(
            message="You can't change the day with a post request."
        ), 400
    return jsonify(
        is_it_friday=(date.today().weekday() == 4),
        this_is_always_friday="https://www.youtube.com/watch?v=kfVsfOSbJY0"
    )


@api.route("/users", methods=["GET"])
def get_users():
    return jsonify(
        users=[user.serialize() for user in User.query.all()]
    )


@api.route('/pets', methods=["GET"])
def get_pets():
    pets = Pet.query.all()
    return jsonify(
        pets=[pet.serialize() for pet in pets]
    ), 200


@api.route('/pets/<int:id>', methods=["GET"])
def get_pet(id):
    """
    You can get info out of the url by using <datatype:variable_name>
    placeholders in the route.

    If you do this, you must have accept a parameter to your
    route function that matches variable_name, for example, if your
    route is '/weather/<str:zip_code>', your function must take an
    argument called zip_code.
    """
    pet = Pet.query.filter_by(id=id).first()
    if pet:
        return jsonify(pet=pet.serialize()), 200
    else:
        return jsonify(
            message=f"No pet with id {id}",
            pet=None
        ), 418


@api.route('/pets', methods=["POST"])
@jwt_required()
def post_pets():
    """
    POST
    BODY: {
        "name": "Little Jerkface",
        "picture_url": "https://placekitten.com/666"
    }

    Response: 204
    =============
    Step 1: get the data from the request via request.json
    Step 2: Make a new instance of our database model.
        We can use keyword arguments or object deconstruction
        to fill the properties of the new db object.
        e.g.: Pet(name="Little Jerkface", ...)
        -or-
        Pet(**request.json) (if your json body matches your property names)
    Step 3: Stage the data into our db session with
        db.session.merge(new_obj) or db.session.add(new_obj)
    Step 4: Commit the changes to the db with db.session.commit()
    """
    pet_data = request.json
    user = User.query.filter_by(email=get_jwt_identity()).first()
    new_pet = Pet(**pet_data)
    user.pets.append(new_pet)
    db.session.merge(user)
    db.session.commit()
    # This is called an empty response:
    return '', 204
