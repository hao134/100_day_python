from flask import Flask, jsonify, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
import random
from functools import wraps

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#The actual decorator function
def required_appkey(viewfunction):
    @wraps(viewfunction)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if request.args.get('key') and request.args.get('key') == "TopSecretAPIKey":
            return viewfunction(*args, **kwargs)
        else:
            abort(403)
            # or jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    return decorated_function

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=True)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
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
        #return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods = ["GET"])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # return jsonify({"cafe":{
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    #     "has_sockets":random_cafe.has_sockets,
    #     "has_toilet":random_cafe.has_toilet,
    #     "has_wifi":random_cafe.has_wifi,
    #     "id":random_cafe.id,
    #     "img_url":random_cafe.img_url,
    #     "location":random_cafe.location,
    #     "map_url":random_cafe.map_url,
    #     "name":random_cafe.name,
    #     "seats":random_cafe.seats,
    # }})

    ##### or ########
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    cafes_dict = {"cafe":[]}
    for cafe in cafes:
        cafes_dict['cafe'].append(cafe.to_dict())
    return jsonify(cafes_dict)
    #### or use list comprehension
    #return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def search():
    location = request.args.get('loc')
    cafes = db.session.query(Cafe).all()
    cafes_dict = {"cafe":[]}
    for cafe in cafes:
        if location.lower() in cafe.location.lower():
            cafes_dict['cafe'].append(cafe.to_dict())
    if cafes_dict["cafe"] == []:
        return jsonify(error={'Not Found': "Sorry, we don't have a cafe at that location."})
    else:
        return jsonify(cafes_dict)


## HTTP POST - Create Record
@app.route("/add", methods= ["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        has_sockets = bool(request.form.get("sockets")),
        has_toilet = bool(request.form.get("toilet")),
        has_wifi = bool(request.form.get("wifi")),
        can_take_calls = bool(request.form.get("calls")),
        seats = request.form.get("seats"),
        coffee_price = request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods = ["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the method. 2000 = Ok
        return jsonify(response = {"success": "Successfully updated the price."})
    else:
        # 404 = Resource not found
        return jsonify(response = {"Not Found": "Sorry a cafe with that id was not found in the database."})

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods = ["DELETE"])
@required_appkey
def delete_coffee(cafe_id):
    #api_key = request.args.get("api_key")
    cafe_to_delete = db.session.query(Cafe).get(cafe_id)
    if cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response = {"success": "Successfully updated the price."})
    else:
        return jsonify(response = {"Not Found": "Sorry a cafe with that id was not found in the database."})



if __name__ == '__main__':
    app.run(debug=True)
