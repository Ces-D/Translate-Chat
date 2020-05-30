from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


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

class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('username_label',
                           validators=[InputRequired(message="Username Required")])
    password = StringField('password_label',
                           validators=[InputRequired(message="Password Required")])