from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<a href='/on'>Turn On</a> \n <a href='/off'>Turn Off</a>"

@app.route("/on")
def turn_on():
    return "<a href='/'>back</a>"

@app.route("/off")
def turn_off():
    return "<a href='/'>back</a>"