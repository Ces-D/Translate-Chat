from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from passlib.hash import pbkdf2_sha256
from TranslateChat.models import *


class RegistrationForm(FlaskForm):
    """Registration Form"""
    username = StringField('username_label',
                           validators=[InputRequired(message="Username Required"),
                                       Length(min=4, max=25,
                                              message="Password must be between 4 and 25 characters")])
    password = PasswordField('password_label',
                             validators=[InputRequired(message="Password Required"),
                                         Length(min=4, max=25,
                                                message="Password must be between 4 and 25 characters")])
    confirm_pswrd = PasswordField('confirm_pswrd_label',
                                  validators=[InputRequired(message="Passwords must match"),
                                              EqualTo('password', message="Passwords must match")])
    submit_button = SubmitField('Create')

    def validate_username(self,username):
        """Validator using SQL Database"""
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists. Select different username")

class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('username_label',
                           validators=[InputRequired(message="Username Required")])
    password = PasswordField('password_label',
                           validators=[InputRequired(message="Password Required")])
    submit_button = SubmitField('Login')

    def validate_credentials(self, username, password):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object is None:
            raise ValidationError("Username or password is incorrect")
        elif not pbkdf2_sha256.verify(password,user_object.password):
            raise ValidationError("Username or password is incorrect")
