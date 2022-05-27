#!/usr/bin/env python3
"""Final Flask Project"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
import sqlite3

app = Flask(__name__)
data = [{
    "student":"Sachin",
    "alias": "Iron man",
    "age" : 35,
    "programming skills": "python"
},
    {
    "student":"Ryan",
    "alias": "Superman",
    "age" : 25,
    "programming skills": "javascript"
}]

#create in memory database so that everytime I run this command, it'll create a fresh new database in RAM
conn=sqlite3.connect(':memory:')
print("Opened database successfully")
with conn:
    conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
    (ID INT PRIMARY KEY     NOT NULL,
    FIRST           TEXT    NOT NULL,
    LAST            TEXT    NOT NULL,
    AGE             INT     NOT NULL,
    SALARY          REAL);''')
    print("Table created successfully")

#creating functions for CRUD operations using sqlite3
c = conn.cursor()
#INSERT sqlite3
with conn:
    c.execute("INSERT INTO COMPANY (ID, FIRST, LAST, AGE, SALARY) VALUES (1, 'Sachin', 'Gurung', '21', 150000)")
    c.execute("INSERT INTO COMPANY (ID, FIRST, LAST, AGE, SALARY) VALUES (2, 'Jane', 'Gurung', '35', 100000)")
    c.execute("INSERT INTO COMPANY (ID, FIRST, LAST, AGE, SALARY) VALUES (3, 'Fake', 'Gurung', '35', 100000)")
    conn.commit()

# show results sqlite3
with conn:
    c.execute("SELECT * FROM COMPANY WHERE LAST = 'Gurung'")
    print(c.fetchall())

# home page route
@app.route("/")
def home():
    return render_template("homepage.html")

# /data route renders data in json format
@app.route("/data")
def userdata():
    return jsonify(data)
    
# this just directs the user to user path
@app.route("/user")
def user():
    return f"<h1>Welcome. You've reached the <u>USER</u> path.</h1>"

# whatever the user types in after /user/..., it will render here "Welcome ..."    
@app.route("/user/<name>")
def anything(name):
    return f"<h1>Welcome {name}!!!<h1>\n"  

# if user enters sachin (case insensitive), it'll render "Hello. Welcome to Jinjapage Sachin! You looking awesome today." 
# if user enters anything else besides sachin, it'll render "You are not Sachin! Please get out of this page... LOSER!!!"
# this logic is in jinjapage.html
@app.route("/<username>")
def index(username):
    return render_template("jinjapage.html", name = username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)