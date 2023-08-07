"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Pet
from api.utils import generate_sitemap, APIException
from datetime import date

api = Blueprint('api', __name__)


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


"""
POST
BODY: {
    "name": "Little Jerkface",
    "user_id": 1,
    "picture_url": "https://placekitten.com/666"
}
"""


@api.route('/pets', methods=["POST"])
def post_pets():
    """
    Step 1: get the data from the request via request.json
    Step 2: Make a new instance of our database model.
        We can use keyword arguments or object deconstruction
        to fill the properties of the new db object.
        e.g.: Pet(name="Little Jerkface", user_id=1, ...)
        -or-
        Pet(**request.json) (if your json body matches your property names)
    Step 3: Stage the data into our db session with
        db.session.merge(new_obj) or db.session.add(new_obj)
    Step 4: Commit the changes to the db with db.session.commit()
    """
    pet_data = request.json
    new_pet = Pet(**pet_data)
    db.session.merge(new_pet)
    db.session.commit()
    # This is called an empty response:
    return '', 204
