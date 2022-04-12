from flask import Flask
app = Flask(__name__)

print(__name__)

# this decorator which is going to make sure that we only trigger this function
# if the user is trying to access the URL, that is homepage ('/')
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'bye'

if __name__ == "__main__":
    app.run()