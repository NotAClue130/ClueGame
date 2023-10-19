# 10/14/2023
# This script holds all the flask events that we will use
# to update the webpage

from flask import request
from flask_socketio import emit

# we will add all the events onto this object, then import 
# this in init
from .extensions import socketio

# This will maintain the users that are in the game. as well as the characters they 
# selected.  We can move these to a relational database per Yang's requirements spec.
dict_sids = {}
dict_characters = {}
# The key of both dict sids and dict characters are username.
# The value of dict sids is sid while the value of characters is character.

# This connection function is from the tutorial: https://www.youtube.com/watch?v=AMp6hlA8xKA
@socketio.on("connect")
def handle_connect():
     print("client connected")

# This adds a player to the player selection view
# note that the game.html enforces that the user name is nonempty
@socketio.on("user_join")
def handle_user_join(username):
    dict_sids[username] = request.sid
    emit("player_joined", broadcast=True)

    # if a new player joins, we need to refresh their screen with all the users that have 
    # previously made selections
    for username_i in dict_characters:
        emit("playerChoice", {"player":dict_characters[username_i], "username": username_i}, broadcast=True)



# This handles the event where a player selectss a character to use
@socketio.on("player_select")
def handle_player_select(character):

    # find the username, this is a bad way to go about it
    username = None
    for username_i in dict_sids:
        if dict_sids[username_i] == request.sid:
            username = username_i
            break

    characters = dict_characters.values()
    usernames = dict_characters.keys()

    # check to make sure another player hasnt chosen this character
    if character in characters:
        return

    # if a player is switching their character
    if username in usernames:
        character_old = dict_characters[username]
        emit("playerChoice", {"player": character_old, "username": ""}, broadcast=True)

    dict_characters[username] = character
    emit("playerChoice", {"player": character, "username": username}, broadcast=True)

# This function starts the game!
@socketio.on("game_start")
def handle_game_start():
    emit("start_game", broadcast=True)
