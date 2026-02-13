import os
from flask import Flask, render_template, request

app = Flask(__name__)


# HOME PAGE 
@app.route("/")
def home():
    return render_template("login.html")  

@app.route("/next", methods=["POST"])
def next_screen():
    username = request.form.get("username")
    return render_template("choice.html", username=username)



@app.route("/sports")
def sports():
    return render_template("sports.html")

@app.route("/watch")
def watch():
    sport = request.args.get("sport")
    return render_template("watch.html", sport=sport)

@app.route("/play")
def play():
    sport = request.args.get("sport")
    return render_template("play.html", sport=sport)

@app.route("/match")
def match():
    return render_template("match.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/watch_match")
def watch_match():
    return render_template("watch_match.html")

@app.route("/last")
def last():
    username = request.args.get("name","Guest")
    return render_template("last.html", username=username)

@app.route("/profile")
def profile():
    username = request.args.get("user", "Guest")
    return render_template("profile.html", username=username)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)
