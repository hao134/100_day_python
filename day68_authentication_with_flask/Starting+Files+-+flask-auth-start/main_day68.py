from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##### Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

@app.route('/')
def home():
    return render_template("index.html", logged_in = current_user.is_authenticated)


@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == 'POST':

        if User.query.filter_by(email=request.form.get('email')).first():
            flash("You've already signed up with that email, log in instead.")
            return redirect(url_for('login'))

        data = request.form
        passwd_hash = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email= request.form.get('email'),
            password = passwd_hash,
            name = data["name"]
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in = current_user.is_authenticated)


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered.
        user = User.query.filter_by(email = email).first()
        #Email doesn't exist
        if not user:
            flash('No this user')
            return redirect(url_for('login'))

        #Check stored password hash against entered password hashed
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        #Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for("secrets"))

    return render_template("login.html",logged_in = current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name = current_user.name, logged_in = current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(
        directory='static/files',
        path = filename,
        as_attachment=False
    )


if __name__ == "__main__":
    app.run(debug=True)
