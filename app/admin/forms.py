from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = StringField("Login", id="login__email", validators=[DataRequired()])
    password = PasswordField("Password", id="login__password", validators=[DataRequired()])
    submit = SubmitField("Submit", id="login__submit")