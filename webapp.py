#!/bin/python3

import paho.mqtt.client as mqtt
from flask import Flask, redirect, url_for

app = Flask(__name__)
a = False

@app.route("/")
def home():
    return "Hello! Welcome to <h1>pomelo<h1>i"

@app.route("/not_welcome")
def not_welcome():
    return "You're not welcome here"

@app.route("/url_input")
def url_input():
    return f"Input URL here"

@app.route("/trigger_builder")
def url_input():
    for i in range(0,10):
        f"Step " + i

    return redirect(url_for())




@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    if a:
        return redirect(url_for("url_input"))
    else:
        return redirect(url_for("not_welcome"))

if __name__ == "__main__":
    app.run()
