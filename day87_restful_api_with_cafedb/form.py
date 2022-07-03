from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField, BooleanField
from wtforms.validators import DataRequired, URL

class UserForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = StringField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label="Sign Me up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField(label = "Log in")

class DeleteForm(FlaskForm):
    password = PasswordField("Delete need password", validators=[DataRequired()])
    submit = SubmitField(label = "Delete it")

class AddCafeForm(FlaskForm):
    password = PasswordField("Edit need password", validators=[DataRequired()])
    cafe_name = StringField(label='Cafe name',validators=[DataRequired()])
    cafe_location = StringField(label='Cafe Location on Google Maps (URL)', validators=[URL(), DataRequired()])
    cafe_image = StringField(label="Cafe's image (URL)", validators=[URL(), DataRequired()])
    location = StringField(label="location name",validators=[DataRequired()])
    has_sockets = BooleanField(label='Sockets?')
    has_toilet = BooleanField(label='toilet?')
    has_wifi = BooleanField(label='wifi?')
    can_take_calls = BooleanField(label='take calls?')
    seats = StringField(label="seats(give a range)",validators=[DataRequired()])
    price = StringField(label="coffe price", validators=[DataRequired()])
    submit = SubmitField(label='Submit')