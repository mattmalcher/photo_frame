from flask import Flask, render_template
from photo_frame import img_db
import os

pic_pth = "../pics/"
db_loc = os.path.join(pic_pth, "photo_frame.db")

if not os.path.isfile(db_loc):
    img_db.init_db(db_loc)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random_image")
def random_img():
    return render_template("random_img.html")


@app.route("/slideshow")
def slideshow():
    return render_template("slideshow.html")


@app.route("/refresh_db")
def refresh():
    images = img_db.find_images(pic_pth)

    for img in images:
        print(img)
        print(img_db.get_date_taken(img))

    return "Refreshing Image Database"
