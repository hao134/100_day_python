from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm
from flask_wtf import FlaskForm
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import stripe
import os

MOVIE_DB_API_KEY = "f23630e371240007466edc8cb63276a5"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://api.themoviedb.org/3/search/movie/https://image.tmdb.org/t/p/w500"
DEFAULT_URL = "/discover/movie?sort_by=popularity.desc"
# stripe keys
stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
stripe_public_key = os.environ["STRIPE_PUBLISHABLE_KEY"]

default_response = requests.get("https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key="+MOVIE_DB_API_KEY)
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

### Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


##CREATE TABLE
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)

db.create_all()

class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    product_id = db.Column(db.String, nullable = False)
    image = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    is_purchased = db.Column(db.Boolean, nullable = False)
    buyer = db.Column(db.String, nullable = False)
db.create_all()

# variables
all_movies = []

@app.route("/", methods = ["GET", "POST"])
def home():
    global all_movies
    all_movies = []
    if request.method == "POST":
        title = request.form.get("movie_name")
        search_response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": title})
        data = search_response.json()
        serch_movies = data["results"]
        all_movies = [movie for movie in serch_movies if movie["poster_path"]]
        return render_template("index.html", movies = all_movies)

    movie_data = default_response.json()
    default_data = movie_data["results"]
    all_movies = [movie for movie in default_data if movie['poster_path']]

    # for i in range(len(all_movies)):
    #     all_movies[i].ranking = len(all_movies) - i
    # db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        already_exist = User.query.filter_by(email=form.email.data).first()
        if not already_exist:
            hash_pass = generate_password_hash(
                form.password.data,
                method = "pbkdf2:sha256",
                salt_length=8
            )
            new_User = User(
                name = form.name.data,
                email = form.email.data,
                password = hash_pass,
                address = form.address.data
            )
            db.session.add(new_User)
            db.session.commit()
            login_user(new_User)
            return redirect(url_for("home"))
        else:
            flash("You've already signed up with that email, log in instead!", 'error')
            return redirect(url_for("login"))
    return render_template("register.html", form = form, current_user=current_user)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        # Email doesn't exist
        if not user:
            flash("No this user",'error')
            return redirect(url_for("login"))

        # Check stored password hash against entered password hashed
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.",'error')
            return redirect(url_for("login"))

        # Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html", form =form, current_user=current_user)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/show-movie/<int:id>")
def show_single_movie(id):
    get_movie = [movie for movie in all_movies if movie["id"] ==id]
    if current_user.is_authenticated:
        book = Cart.query.filter_by(buyer=current_user.email, is_purchased=False, product_id=id).first()
        if book:
            message = "Added to cart"
        else:
            message = ""
    else:
        message = ""
    return render_template("single_movie.html", movie=get_movie[0],
                           authenticated = current_user.is_authenticated, message=message)

@app.route("/add-to-cart/<int:id>")
def add_to_cart(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    get_movie  = [movie for movie in all_movies if movie["id"] == id]
    movie = get_movie[0]
    new_cart_item = Cart(
        product_id =movie["id"],
        title=movie["title"],
        image="https://image.tmdb.org/t/p/w500"+movie["poster_path"],
        price=2,
        is_purchased=False,
        buyer=current_user.email
    )
    db.session.add(new_cart_item)
    db.session.commit()
    return redirect(url_for('show_single_movie', id = id))

@app.route("/cart")
def show_cart():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    global payable_amount
    global cart_list
    cart_list = ""
    total_price = 0
    all_items = Cart.query.filter_by(buyer = current_user.email, is_purchased = False).all()
    for item in all_items:
        total_price += item.price
    discount = 1
    if len(all_items) >= 5:
        for _ in range(int(len(all_items)/5)):
            discount *= 0.8
    payable_amount = int(total_price * discount)
    cart_list = ",".join([item.title for item in all_items])
    return render_template("cart.html", cart=all_items, total_price = total_price, payable_amount=payable_amount,
                           public_key = stripe_public_key, authenticated=current_user.is_authenticated)

@app.route("/delete/<int:id>")
def delete_item(id):
    item = Cart.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("show_cart"))

@app.route("/create-checkout-session", methods=["POST"])
@login_required
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data":{
                "currency":"usd",
                "product_data":{
                    "name":cart_list,
                },
                "unit_amount":payable_amount*100,
            },
            "quantity":1,
        }],
        mode="payment",
        success_url=domain_url+"success",
        cancel_url=domain_url+"failed"
    )
    response = jsonify({"id":session.id})
    return response

@app.route("/success")
@login_required
def success():
    global cart_list
    non_purchased_items = Cart.query.filter_by(buyer=current_user.email, is_purchased=False).all()
    for item in non_purchased_items:
        id = item.id
        movie = Cart.query.get(int(id))
        movie.is_purchased = True
        db.session.commit()
    cart_list=""
    return render_template("success.html", authenticated=current_user.is_authenticated)

@app.route("/failed")
@login_required
def failed():
    return render_template("cancel.html", authenticated=current_user.is_authenticated)

if __name__ == '__main__':
    app.run(debug=True)