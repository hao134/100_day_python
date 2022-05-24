from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('abc.html')

@app.route('/user/<username>')
def username(username):
    return 'i am ' + username

@app.route('/a')
def url_for_a():
    return 'here is a'

@app.route('/b')
def b():
    return redirect(url_for('url_for_a'))

if __name__ == '__main__':
    app.debug = True
    app.run()