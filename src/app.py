"""
File: app.py
File-Path: src/app.py
Author: Thomas Bruce
Date-Created: 09-29-2025

Description:
    Base of Flask app
    THIS WILL NOT WORK UNTIL SCHEMAS HAVE BEEN CREATED!!!
    ALL HIGHER-LEVEL SQL FUNCTIONALITY HAS BEEN OMITTED 

Inputs:
    <External sources this script uses (ex: files, database, APIs)>

Outputs:
    <External results this script produces (ex: files, database updates, API responses, logs)>
"""

from flask import Flask, render_template

from db.server import engine, Base

# schema imports
from db.schema import household, recipe, user, member

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
