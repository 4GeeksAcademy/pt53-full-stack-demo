
from itertools import chain
import click
import json
import random
import string
from tqdm import tqdm
from time import sleep
from api.models import db, User, Pet, Rating

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with your database, for example: Import the price of bitcoin every night as 12am
"""


def setup_commands(app):
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("insert-test-users")  # name of our command
    @click.argument("count")  # argument of out command
    def insert_test_data(count):
        print("Creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.email = "test_user" + str(x) + "@test.com"
            user.password = "123456"
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            print("User: ", user.email, " created.")

        print("All test users created")

        # Insert the code to populate others tables if needed

    @app.cli.command("popdb")
    def populate_db():
        """
        TBD (while you are in breakout rooms.)
        """
        with open("./src/api/testdata.json", "rt") as test_data:
            data = json.load(test_data)

            for user in tqdm(data["users"]):
                db.session.merge(User(
                    id=user["id"],
                    email=user["email"],
                    password=''.join(random.choices(string.ascii_letters, k=8))
                ))
            db.session.commit()

            for pet in tqdm(data["pets"]):
                db.session.merge(Pet(
                    id=pet["id"],
                    name=pet["name"],
                    picture_url=pet["picture_url"],
                ))
            db.session.commit()

            for rating in tqdm(data["ratings"]):
                db.session.merge(Rating(
                    id=rating["id"],
                    user_id=rating["user_id"],
                    cuteness=rating["cuteness"],
                    goodness=rating["goodness"],
                    precociousness=rating["precociousness"],
                ))
            db.session.commit()
