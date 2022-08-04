from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
import extcolors
from colormap import rgb2hex


app = Flask(__name__)

UPLOAD_FOLDER = "static/img/"
app.secret_key="secret_key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
Bootstrap5(app)

ALLOWED_ENTENSIONS = set(["png", "jpg", "jpeg", "gif"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_ENTENSIONS
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def upload_image():
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        flash("No image selected for uploading")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        full_file_path = UPLOAD_FOLDER+filename
        colors_x = extcolors.extract_from_path(full_file_path, tolerance=12, limit=12)
        colors_pre_list = str(colors_x).replace('([(', '').split(', (')[0:-1]
        df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
        df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),
                               int(i.split(", ")[1]),
                               int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]
        flash("Image successfully uploaded and displayed below")
        return render_template("index.html", filename=filename, hash_colors = df_color_up)
    else:
        flash("Allowed image types are - png, jpg, jpeg, gif")
        return redirect(request.url)

@app.route("/display/<filename>")
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == "__main__":
    app.run()
