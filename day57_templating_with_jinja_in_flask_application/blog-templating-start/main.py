from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/64f1b582343677fe0d71"
response = requests.get(blog_url)
all_posts = response.json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<num>')
def post_blog(num):
    the_post = all_posts[int(num)-1]
    return render_template("post.html", post_text = the_post)


if __name__ == "__main__":
    app.run(debug=True)
