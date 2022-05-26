from flask import Flask
#  from flask.ext.sqlalchemy import SQLAlchemy<--新版取消了
from flask_sqlalchemy import SQLAlchemy
import os

#  取得目前文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#  新版本的部份預設為none，會有異常，再設置True即可。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  設置sqlite檔案路徑
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(pjdir, 'data.sqlite')

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #  設置關聯，relationship設置於一對多的『一』
    contacts = db.relationship('Contact', backref='useruser')

    def __repr__(self):
        return '<User %r>' % self.username


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    contact_style = db.Column(db.String)
    contact_context = db.Column(db.String)
    #  設置外來鍵，ForeignKey設置於一對多的『多』
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return 'contact_style:%s, contact_context:%s' % \
               (self.contact_style, self.contact_context)

db.create_all()