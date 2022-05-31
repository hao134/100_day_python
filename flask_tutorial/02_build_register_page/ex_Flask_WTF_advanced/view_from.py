from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

# 從繼承FlaskFrom開始
class UserForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(message='Not Null')])
    email = StringField('Email', validators=[DataRequired(message='Not Null'), Email()])
    submit = SubmitField('Submit')
