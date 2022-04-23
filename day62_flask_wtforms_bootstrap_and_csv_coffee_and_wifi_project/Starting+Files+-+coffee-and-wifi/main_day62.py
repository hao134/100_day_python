from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
COFFEE_RATING = [('✘','✘'),('☕','☕'),('☕☕','☕☕'),('☕☕☕','☕☕☕'),('☕☕☕☕','☕☕☕☕'),('☕☕☕☕☕','☕☕☕☕☕')]
WIFI_RATING = [('✘','✘'),('💪','💪'),('💪💪','💪💪'),('💪💪💪','💪💪💪'),('💪💪💪💪','💪💪💪💪'),('💪💪💪💪💪','💪💪💪💪💪')]
POWER_RATING = [('✘','✘'),('🔌','🔌'),('🔌🔌','🔌🔌'),('🔌🔌🔌','🔌🔌🔌'),('🔌🔌🔌🔌','🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌','🔌🔌🔌🔌🔌')]
class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    cafe_location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = TimeField(label='Opening Time e.g.8AM')
    close_time = TimeField(label='Closing Time e.g.17:30PM')
    coffee_rating = SelectField(label='Coffee Rating', choices=COFFEE_RATING)
    wifi_strength_rating = SelectField(label='Wifi Strength Rating', choices=WIFI_RATING)
    power_socket_availability = SelectField(label='Power Socket Availability', choices=POWER_RATING)
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    #row = ['Lighthaus','https://goo.gl/maps/2EvhB4oq4gyUXKXx9','11AM', '3:30PM','cccc','vvv','aa']
    if form.validate_on_submit():
        row = [form.cafe.data, form.cafe_location.data, form.open_time.data,form.close_time.data, form.coffee_rating.data,form.wifi_strength_rating.data,form.power_socket_availability.data]
        with open('./cafe-data.csv','a',newline='\n') as f:
            writer_object = csv.writer(f)
            writer_object.writerow(row)
        return redirect(url_for('cafes'))
        #return render_template('cafes.html')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html',form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
