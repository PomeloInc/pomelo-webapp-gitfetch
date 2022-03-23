#!/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Welcome to <h1>pomelo<h1>i"

if __name__ == "__main__":
    app.run()
