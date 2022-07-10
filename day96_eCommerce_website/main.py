from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm
from flask_wtf import FlaskForm
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import requests

MOVIE_DB_API_KEY = "f23630e371240007466edc8cb63276a5"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://api.themoviedb.org/3/search/movie/https://image.tmdb.org/t/p/w500"
DEFAULT_URL = "/discover/movie?sort_by=popularity.desc"
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


@app.route("/", methods = ["GET", "POST"])
def home():
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


if __name__ == '__main__':
    app.run(debug=True)