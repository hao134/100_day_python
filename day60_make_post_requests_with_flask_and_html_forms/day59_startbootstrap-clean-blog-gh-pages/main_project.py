from flask import Flask, render_template, request
import requests
from post import Post
import smtplib
import os

MY_EMAIL = os.environ.get("MY_MAIL")
MY_PASSWORD = os.environ.get("MY_PSWD")
Sent_Email = os.environ.get("S_EMAIL")

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

@app.route("/contact", methods = ["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["phone"])
        print(data["email"])
        print(data["message"])
        if data["email"] != "":
            send_email(data["name"],data["email"],data["phone"],data["message"])
            return render_template("contact.html", msg_sent = True, success_words = "Successfully sent your message")
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=Sent_Email, msg=email_message)

if __name__ == "__main__":
    app.run(debug=True)