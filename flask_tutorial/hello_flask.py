from flask import Flask, url_for, redirect, render_template, request, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

def login_check(username, password):
    if username == 'admin' and password == 'hello':
        return True
    else:
        return False

@app.route('/loginurl', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'], request.form['password']):
            flash('Login Success!')
            return redirect(url_for('hello', username=request.form.get('username')))
    return render_template('login.html')

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)