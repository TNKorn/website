# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello!! :), from Tayra"


@app.route("/today")
def hello_world_today():
    return str(date.today())


@app.route("/apple")
def hello_world_apple():
    return "This is an apple"
