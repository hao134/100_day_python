from flask import Flask, render_template
from view_from import UserForm

app = Flask(__name__)
app.secret_key = '\x17\xc5=\xaf\x98\x16]\xa8\xb5x\x9f6'

@app.route("/user", methods=["GET", "POST"])
def user():
    form = UserForm()
    # flask_wtf類別中提供判斷是否表單提交過來的method, 不需要自行利用request.method來判斷
    if form.validate_on_submit():
        return 'Success Submit'

    # 如果不是提交過來的表單，就是GET，這時候就回傳user.html網頁
    return render_template('user.html', form = form)

if __name__ == '__main__':
    app.debug = True
    app.run()