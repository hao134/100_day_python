from flask import Flask, flash, render_template, request, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask_bootstrap import Bootstrap5
from form import DeleteForm,AddCafeForm

app = Flask(__name__)
Bootstrap5(app)
app.config["SECRET_KEY"] = "shihhao"

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=True)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, default=False, server_default="false",nullable=False)
    has_wifi = db.Column(db.Boolean, default=False, server_default="false",nullable=False)
    has_sockets = db.Column(db.Boolean, default=False, server_default="false",nullable=False)
    can_take_calls = db.Column(db.Boolean, default=False, server_default="false",nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry:
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

    ##### or #######
    # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    all_cafes = Cafe.query.all()
    return render_template("index.html", all_posts = all_cafes)

@app.route("/cafes")
def cafes():
    all_cafes = Cafe.query.all()
    return render_template("cafes.html",all_posts = all_cafes)

@app.route("/delete/<int:cafe_id>", methods = ["POST", "GET"])
def delete_cafe(cafe_id):
    form = DeleteForm()
    if form.validate_on_submit():
        if form.password.data != "123456":
            flash("Password wrong, try again")
            return redirect(url_for("delete_cafe", cafe_id = cafe_id))
        cafe_to_delete = Cafe.query.get(cafe_id)
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("delete.html", form = form)

@app.route("/add", methods = ["POST", "GET"])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        if form.password.data != "123456":
            flash("Password wrong, try again!")
            return redirect(url_for("add_cafe"))
        new_cafe = Cafe(
            name = form.cafe_name.data,
            map_url = form.cafe_location.data,
            img_url = form.cafe_image.data,
            location = form.location.data,
            seats = form.seats.data,
            has_toilet=form.has_toilet.data,
            has_wifi = form.has_wifi.data,
            has_sockets = form.has_sockets.data,
            can_take_calls = form.can_take_calls.data,
            coffee_price = form.price.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make_cafe.html", form = form)


@app.route("/edit/<int:cafe_id>",methods = ["POST", "GET"])
def edit(cafe_id):
    cafe_to_edit = Cafe.query.get(cafe_id)
    edit_form = AddCafeForm(
        cafe_name=cafe_to_edit.name,
        cafe_location=cafe_to_edit.map_url,
        cafe_image=cafe_to_edit.img_url,
        location=cafe_to_edit.location,
        seats=cafe_to_edit.seats,
        has_toilet=cafe_to_edit.has_toilet,
        has_wifi=cafe_to_edit.has_wifi,
        has_sockets=cafe_to_edit.has_sockets,
        can_take_calls=cafe_to_edit.can_take_calls,
        price=cafe_to_edit.coffee_price
    )
    if edit_form.validate_on_submit():
        if edit_form.password.data != "123456":
            flash("Password wrong, try again")
            return redirect(url_for("edit", cafe_id=cafe_id))
        cafe_to_edit.name = edit_form.cafe_name.data
        cafe_to_edit.map_url = edit_form.cafe_location.data
        cafe_to_edit.img_url = edit_form.cafe_image.data
        cafe_to_edit.location = edit_form.location.data
        cafe_to_edit.seats = edit_form.seats.data
        cafe_to_edit.has_toilet = edit_form.has_toilet.data
        cafe_to_edit.has_wifi = edit_form.has_wifi.data
        cafe_to_edit.has_sockets = edit_form.has_sockets.data
        cafe_to_edit.can_take_calls = edit_form.can_take_calls.data
        cafe_to_edit.coffee_price = edit_form.price.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make_cafe.html", form = edit_form)



if __name__ == '__main__':
    app.run(debug=True)