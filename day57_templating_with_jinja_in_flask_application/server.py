from flask import Flask, render_template
import random
import datetime
import requests

# parameter = {"name":"jason"}
# name_year = requests.get("https://api.agify.io/",params=parameter)
# name_gender = requests.get("https://api.genderize.io/",params=parameter)
# print(name_year.json()["age"])
# print(name_gender.json()["gender"])
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(0, 9)
    this_year = datetime.datetime.now().year
    return render_template("index.html",num=random_number, year = this_year)

@app.route('/guess/<person_name>')
def guess(person_name):
    parameter = {"name": person_name}
    name_year = requests.get("https://api.agify.io/", params=parameter)
    name_gender = requests.get("https://api.genderize.io/", params=parameter)
    person_gender = name_gender.json()["gender"]
    person_year = name_year.json()["age"]
    return render_template("name_data.html",name = person_name, gender = person_gender, year = person_year)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/64f1b582343677fe0d71"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)




if __name__ == "__main__":
    app.run(debug=True)


