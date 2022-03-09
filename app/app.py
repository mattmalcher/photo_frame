from flask import Flask, render_template, send_file, request
from photo_frame import img_db
import os
import urllib.parse

pic_pth = "../pics/"
# db_loc = os.path.join(pic_pth, "photo_frame.db")
db_loc = "../db/photo_frame.db"

if not os.path.isfile(db_loc):
    img_db.init_db(db_loc)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/disk_img/")
def disk_img():
    filename = request.args.get("filename")
    print(filename)
    return send_file(filename)


@app.route("/random_image")
def random_img():

    path, fname, date = img_db.get_random_path(db_loc=db_loc)
    enc_path = urllib.parse.quote(path)

    return render_template(
        "random_img.html", path=path, enc_path=enc_path, fname=fname, date=date
    )


@app.route("/slideshow/<seconds>")
def slideshow(seconds):
    path, fname, date = img_db.get_random_path(db_loc=db_loc)
    enc_path = urllib.parse.quote(path)

    return render_template("slideshow.html", enc_path=enc_path, seconds=seconds)


@app.route("/refresh_db")
def refresh():

    img_db.find_images(pic_pth, db_loc=db_loc)

    return "Refreshing Image Database"
