from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

### Decorate function
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if current_user.id == 1:
                return f(*args, **kwargs)
            else:
                abort(403)
        except AttributeError:
            abort(404)
    return decorated_function

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "shihhao"
api = Api(app)

# @app.before_first_request
# def create_table():
#     db.create_all()

