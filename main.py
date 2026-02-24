from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def vrni():
    return render_template("index.html")

@app.route("/coinFlip")
def coinFlip():
    return render_template("coinFlip.html")

@app.route("/coinData")
def coinData():
    rnd = random.randint(0, 1)
    return ["heads","tails"][rnd]


app.run(debug = True)