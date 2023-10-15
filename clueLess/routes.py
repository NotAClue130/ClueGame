# This routes function follows the tutorial: https://www.youtube.com/watch?v=AMp6hlA8xKA
# it initializes the website according to the template, game.html

from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("game.html")