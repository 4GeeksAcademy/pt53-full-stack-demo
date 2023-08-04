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
    pet = Pet.query.filter_by(id=id).first()
    if pet:
        return jsonify(pet=pet.serialize()), 200
    else:
        return jsonify(
            message=f"No pet with id {id}",
            pet=None
        ), 418


@api.route('/pets', methods=["POST"])
def post_pets():
    pet_data = request.json
    new_pet = Pet(**pet_data)
    db.session.merge(new_pet)
    db.session.commit()
    return '', 204
