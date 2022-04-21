from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Play with me"

    text = """It is a place where your dreams come true"""

    choices = [
        ('first_page',"Play"),
        ('run_away',"Go away")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/game")
def first_page():
    title = "You chose to play"
    
    text = """Feel free to choose one of my magic boxes"""

    choices = [
        ('firstbox',"Choose box #1"),
        ('secondbox',"Choose box #2"),
        ('run_away', "Go away")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "You run away!"
    
    text = """You chose not to try out your luck!"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/box1")
def firstbox():
    title = "You lost!"
    
    text = """This box is empty. Try out your luck somewhere else"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/box2")
def secondbox():
    title = "You won!"
    
    text = """Your prize is hidden, try to find it"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)