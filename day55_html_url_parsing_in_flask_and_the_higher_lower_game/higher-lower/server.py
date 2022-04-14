from flask import Flask
import random
app = Flask(__name__)

random_int = random.randint(0, 9)

# Thanks the code from RedJuly
# https://gist.github.com/angelabauer/26eb9190a094761a9f49b22e8ee4c0fb?permalink_comment_id=3729863#gistcomment-3729863
def checker_decorator(fn):
    def wrapper(number):
        if int(number) == random_int:
            return fn(number)
        elif int(number) < random_int:
            return '<h1 style="color: red">Too low, try again!</h1>' \
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
        else:
            return '<h1 style="color: purple">Too high, try again!</h1>' \
                   '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    return wrapper



@app.route('/')
def show_number():
    return "<h1>Guess a number between 0 and 9</h1>"\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
@checker_decorator
def correct(number):
    return f'<h1 style="color: green">You found me!, the correct number is {number}</h1>' \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

# def compare_number(guessed_number, rand_num = random_int):
#     if guessed_number > rand_num:
#         return '<h1 style="color: purple">Too high, try again!</h1>' \
#                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
#     elif guessed_number < rand_num:
#         return '<h1 style="color: red">Too low, try again!</h1>' \
#                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
#     else:
#         return '<h1 style="color: green">You found me!</h1>' \
#                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)