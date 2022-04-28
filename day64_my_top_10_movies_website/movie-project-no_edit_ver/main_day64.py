from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies-collection.db'
# silence the warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

## CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique= True, nullable = False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(500), nullable = False)
    rating = db.Column(db.Float, nullable = True)
    ranking = db.Column(db.Integer, nullable = True)
    review = db.Column(db.String(250), nullable = True)
    img_url = db.Column(db.String(250), nullable = False)

    def __repr__(self):
        return f'<Movie {self.title}>'

db.create_all()

## CREATE MOVIE
# class MovieEditForm(FlaskForm):
#     change_rating = StringField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
#     change_review = StringField(label='Your Review',validators=[DataRequired()])
#     submit = SubmitField(label = 'Submit')
#
# class MovieAddForm(FlaskForm):
#     movie_title = StringField(label='Movie Title', validators=[DataRequired()])
#     submit = SubmitField(label = "Add Movie")



# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating)
    i = 1
    for movie in all_movies[::-1]:
        movie.ranking = i
        db.session.commit()
        i += 1
    return render_template("index.html", movies = all_movies)

# @app.route("/edit", methods = ["GET", "POST"])
# def edit():
#     form = MovieEditForm()
#     movie_id = request.args.get('index')
#     movie_to_update = Movie.query.get(movie_id)
#     if form.validate_on_submit():
#         movie_to_update.rating = form.change_rating.data
#         movie_to_update.review = form.change_review.data
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template('edit.html', movie = movie_to_update, form=form)

# @app.route("/delete")
# def delete():
#     movie_id = request.args.get('index')
#     # DELETE A RECORD BY ID
#     movie_to_delete = Movie.query.get(movie_id)
#     db.session.delete(movie_to_delete)
#     db.session.commit()
#     return redirect(url_for('home'))

# @app.route("/add",methods = ["GET", "POST"])
# def add_movie():
#     form = MovieAddForm()
#     api_key = "f23630e371240007466edc8cb63276a5"
#     if form.validate_on_submit():
#         quest = form.movie_title.data
#         parameters = {
#             "query": quest,
#             "api_key": api_key
#         }
#         response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters)
#         movie_data = response.json()["results"]
#         return render_template('select.html', data = movie_data)
#     return render_template('add.html', form=form)

# @app.route("/find")
# def find_movie():
#     id = request.args.get('id')
#     api_key = "f23630e371240007466edc8cb63276a5"
#     if id:
#         parameters = {
#             "api_key": api_key,
#             "language": "en-US"
#         }
#         response = requests.get(f"https://api.themoviedb.org/3/movie/{id}", params=parameters)
#         movie_data = response.json()
#         new_movie = Movie(
#             title=movie_data['title'],
#             year=int(movie_data["release_date"][:4]),
#             description=movie_data["overview"],
#             rating = 0.0,
#             ranking = 'None',
#             review = 'None',
#             img_url="https://image.tmdb.org/t/p/w500/" + movie_data["poster_path"]
#         )
#         db.session.add(new_movie)
#         db.session.commit()
#         return redirect(url_for('edit',index = new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
