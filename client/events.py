# 10/14/2023
# This script holds all the flask events that we will use
# to update the webpage

from flask import request
from flask_socketio import emit

# we will add all the events onto this object, then import
# this in init
from .extensions import socketio

# This will base the events on database
from .sql import *
import pymysql
from dbAccount import*


db = pymysql.connect(host='localhost', port=3306, user=usr, password=pwd, db='NotAClue', charset='utf8')

# This connection function is from the tutorial: https://www.youtube.com/watch?v=AMp6hlA8xKA
@socketio.on("connect")
def handle_connect():
     print("client connected in sql eventss")

# This adds a player to the player selection view
# note that the game.html enforces that the user name is nonempty
@socketio.on("user_join")
def handle_user_join(username):
    SQL_handle_user_join(db, request.sid, username)
    emit("player_joined", broadcast=True)

    # if a new player joins, we need to refresh their screen with all the users that have
    # previously made selections
    for character, username in SQL_get_characters_and_usernames(db):
        emit("playerChoice", {"player": character, "username": username}, broadcast=True)



# This handles the event where a player selectss a character to use
@socketio.on("player_select")
def handle_player_select(character):
    # "playerName" is synonymous with "character"
    # find the username, this is a bad way to go about it
    username = SQL_get_username_based_on_sid(db, request.sid)
    characters_and_usernames = SQL_get_characters_and_usernames(db)
    characters = [i[0] for i in characters_and_usernames]
    usernames = [i[1] for i in characters_and_usernames]

    # check to make sure another player hasnt chosen this character
    if character in characters:
        return

    # if a player is switching their character
    if username in usernames:
        character_old = SQL_get_character_based_on_username(db, username)
        SQL_delete_character_based_on_charactername(db, character_old)
        emit("playerChoice", {"player": character_old, "username": ""}, broadcast=True)

    SQL_handle_player_select(db, character, request.sid)
    emit("playerChoice", {"player": character, "username": username}, broadcast=True)

# This function starts the game!
@socketio.on("game_start")
def handle_game_start():
    emit("start_game", broadcast=True)