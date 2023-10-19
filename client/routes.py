# This routes function follows the tutorial: https://www.youtube.com/watch?v=AMp6hlA8xKA
# it initializes the website according to the template, game.html

from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def entry():
    return render_template("entry.html")

@main.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@main.route("/board", methods=["GET"])
def board():
    return render_template("board.html")

