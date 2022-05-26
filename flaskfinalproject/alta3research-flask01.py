#!/usr/bin/env python3
"""Final Flask Project"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template

app = Flask(__name__)
data = [{
    "student":"Sachin",
    "alias": "Iron man",
    "age" : 35,
    "programming skills": [
        "python",
        "flask",
        "api",
        "java"
    ]
}]

@app.route("/data")
def index():
    return jsonify(data)
    

@app.route("/user")
def user():
    return ("Welcome User. Your path is /user.")
    
@app.route("/user/<name>")
def anything(name):
    return f"<h1>Welcome {name}<h1>\n"  

@app.route("/<username>")
def index(username):
    return render_template("jinjapage.html", name = username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)