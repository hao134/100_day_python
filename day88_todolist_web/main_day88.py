from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import timezone, datetime, timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"
Bootstrap5(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoList.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class todoList(db.Model):
    __tablename__ = "todoList"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    is_completed = db.Column(db.Boolean, nullable = False)
    date = db.Column(db.String(250), nullable = False)
db.create_all()


@app.route("/", methods = ["GET", "POST"])
def home():
    db_todo_lists = todoList.query.all()
    total_nums= len(db_todo_lists)
    completed_nums = 0
    uncompleted_nums = 0
    for item in db_todo_lists:
        if item.is_completed == False:
            uncompleted_nums += 1
        else:
            completed_nums += 1
    if request.method == "POST":
        TITLE = request.form['todo_list']
        tz = timezone(timedelta(hours=+8))
        new_todolist = todoList(
            title = TITLE,
            date = datetime.now(tz).strftime("%H:%M:%S %B %d,%Y"),
            is_completed = False,
        )
        db.session.add(new_todolist)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("index.html", lists = db_todo_lists, nums_total = total_nums, nums_completed=completed_nums, nums_uncompleted = uncompleted_nums)

@app.route("/update/<int:list_id>")
def update(list_id):
    list_to_update = todoList.query.get(list_id)
    list_to_update.is_completed = True
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/delete/<int:list_id>")
def delete(list_id):
    list_to_delete = todoList.query.get(list_id)
    db.session.delete(list_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)