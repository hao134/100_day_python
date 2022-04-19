from flask import Flask, render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/1d5a45f9192f7fc4b70b").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"],post["body"],post["title"], post["subtitle"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts = post_objects)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html",post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)