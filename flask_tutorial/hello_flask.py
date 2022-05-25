from flask import Flask, url_for, redirect, render_template, request
app = Flask(__name__)

@app.route('/loginurl', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return "Hello " + request.values['username']

    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()