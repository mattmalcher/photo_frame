from flask import Flask, render_template

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
    return "Refreshing Image Database"
