
import os
from flask_admin import Admin
from .models import db, User, Pet, Rating
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField


class UserView(ModelView):
    column_list = ['email', 'is_active']
    column_editable_list = ['is_active',]
    column_exclude_list = ['_password', ]
    form_extra_fields = {
        'password': PasswordField('password')
    }


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'slate'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap4')

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Pet, db.session))
    admin.add_view(ModelView(Rating, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
