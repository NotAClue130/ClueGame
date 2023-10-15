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
users = {}
characters = {}

# This connection function is from the tutorial: https://www.youtube.com/watch?v=AMp6hlA8xKA
@socketio.on("connect")
def handle_connect():
    print("Client connected!")

# This adds a player to the player selection view
@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined!")
    users[username] = request.sid

    # if a new player joins, we need to refresh their screen with all the users that have 
    # previously made selections
    for user in characters:
        emit("playerChoice", {"player":characters[user], "username": user}, broadcast=True)


# This handles the event where a player selectss a character to use
@socketio.on("player_select")
def handle_player_select(playerName):
    username = None 
    for user in users:
        if users[user] == request.sid:
            username = user  
            characters[user] = playerName      
    emit("playerChoice", {"player":playerName, "username": username}, broadcast=True)


# This function starts the game!
@socketio.on("game_start")
def handle_game_start():
    print('game starting')
    emit("start_game", broadcast=True)
