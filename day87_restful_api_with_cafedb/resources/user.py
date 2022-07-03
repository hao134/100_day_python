import sqlite3
from flask import render_template, redirect, url_for
from flask_restful import Resource
from models.user import  UserModel
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = StringField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label="Sign Me up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField(label = "Log in")

class UserRegister(Resource):
    def register(self):
        form = UserForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            connection = sqlite3.connect("cafes.db")
            cursor = connection.cursor()

            query = "INSERT INTO users VALUES (NULL, ?, ?)"
            cursor.execute(query, (username, password))

            connection.commit()
            connection.close()
            return redirect(url_for())
        return render_template("register.html")
