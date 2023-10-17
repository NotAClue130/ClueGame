# 10/14/2023
# This script holds all the flask events that we will use
# to update the webpage

from flask import request
from flask_socketio import emit

# we will add all the events onto this object, then import 
# this in init
from .extensions import socketio

# This will base the events on database
from sql import *
import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='database', charset='utf8')

# This will maintain the users that are in the game. as well as the characters they 
# selected.  We can move these to a relational database per Yang's requirements spec.
create_table_of_users(db)
create_table_of_characters(db)

# This connection function is from the tutorial: https://www.youtube.com/watch?v=AMp6hlA8xKA
@socketio.on("connect")
def handle_connect():
     print("client connected")

# This adds a player to the player selection view
# note that the game.html enforces that the user name is nonempty
@socketio.on("user_join")
def handle_user_join(username):
    insert_table_users(db, username, request.sid)
    emit("player_joined", broadcast=True)

    # if a new player joins, we need to refresh their screen with all the users that have 
    # previously made selections
    character_user_list=query_table_characters(db)
    for character, user in character_user_list:
        emit("playerChoice", {"player":character, "username": user}, broadcast=True)



# This handles the event where a player selectss a character to use
@socketio.on("player_select")
def handle_player_select(playerName):
    username = None 

    # find the username, this is a bad way to go about it
    username = query_table_users_on_sid(request.sid)
    character_user_list = query_table_characters(db)
    characters = [i[0] for i in character_user_list]
    usernames = [i[1] for i in character_user_list]
    # check to make sure another player hasnt chosen this character
    if playerName not in characters:
        # if a player is switching their character
        if username in usernames:
            oldChar = query_table_characters_on_username(db,username)
            emit("playerChoice", {"player":oldChar, "username": ""}, broadcast=True)

        insert_table_characters(playerName, username)
        emit("playerChoice", {"player":playerName, "username": username}, broadcast=True)

# This function starts the game!
@socketio.on("game_start")
def handle_game_start():
    emit("start_game", broadcast=True)
