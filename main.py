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
    # v primeru POST print(request.form)
    print(request.args["vrednost"])
    rnd = random.randint(0, 1)
    status = ["heads","tails"][rnd]
    return {"img": "https://i.postimg.cc/CBNJNfDJ/head.png", "status": status} if status == "heads" else {"img": "https://i.postimg.cc/zysdXN8w/tail.png", "status": status}

@app.route("/randomQuote")
def randomQuote():
    return render_template("randomQuote.html")

@app.route("/randomQuoteData")
def randomQuoteData():
    quotes = [
    {"quote": "Sometimes you win, sometimes you learn", "author": "John C. Maxwell"},
    {"quote": "The only way to do great work is to love what you do", "author": "Steve Jobs"},
    {"quote": "Success is not the key to happiness. Happiness is the key to success", "author": "Albert Schweitzer"},
    {"quote": "In the middle of difficulty lies opportunity", "author": "Albert Einstein"},
    {"quote": "Do not wait to strike till the iron is hot, but make it hot by striking", "author": "William Butler Yeats"},
    {"quote": "I find that the harder I work, the more luck I seem to have", "author": "Thomas Jefferson"},
    {"quote": "It does not matter how slowly you go as long as you do not stop", "author": "Confucius"},
    {"quote": "The best way to predict the future is to create it", "author": "Abraham Lincoln"},
    {"quote": "Your time is limited, so don’t waste it living someone else’s life", "author": "Steve Jobs"},
    {"quote": "What you get by achieving your goals is not as important as what you become by achieving your goals", "author": "Zig Ziglar"}
]
    random_quote = random.choice(quotes)
    return {"quote": random_quote["quote"], "author": random_quote["author"]}

app.run(debug = True)