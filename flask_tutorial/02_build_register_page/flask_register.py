from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os


pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'data_register.sqlite')
app.secret_key = '\x17\xc5=\xaf\x98\x16]\xa8\xb5x\x9f6'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

@app.route('/register', methods=["GET", "POST"])
def register():
    from model import UserRegister
    from form import FormRegister
    form = FormRegister()
    if form.validate_on_submit():
        user = UserRegister(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return 'Success Thank You'
    return render_template("register.html", form = form)

if __name__ == "__main__":
    app.debug = True
    app.run()

