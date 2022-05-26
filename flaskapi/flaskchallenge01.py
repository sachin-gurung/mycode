from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("flaskchallenge01.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = "defaultuser"
    elif request.method == "GET":
        if request.args.get("nm"):
            user = request.args.get("nm")
        else: 
            user = "defaultuser"
    return redirect(url_for("home"))



@app.route("/answer")
def answer():
    return "answer page"

@app.route("/correct")
def correct():
    return "correct page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

