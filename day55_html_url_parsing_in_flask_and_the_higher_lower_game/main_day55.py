from flask import Flask
app = Flask(__name__)

print(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# this decorator which is going to make sure that we only trigger this function
# if the user is trying to access the URL, that is homepage ('/')
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p style="text-align: center">This is a paragraph.</p>' \
           '<img src="http://pic.happytify.cc/uploads/20210409/95/C957AA36A2C4w1077h1104.jpeg">' \




@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'bye'

@app.route("/<name>/<int:number>")
def greet(name,number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)