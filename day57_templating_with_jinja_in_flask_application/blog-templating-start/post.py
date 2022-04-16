import requests
class Post:
    def __init__(self):
        blog_url = "https://api.npoint.io/64f1b582343677fe0d71"
        response = requests.get(blog_url)
        self.all_posts = response.json()


