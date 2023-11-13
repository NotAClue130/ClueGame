# 10/14/2023
# This script holds all the flask events that we will use
# to update the webpage

# Chuan Lin: I am sorry that I don't know how to get the game_global instance created in run.py
# from run import game_global
# from backend.Character import mapping_from_character_to_locations

from flask import request
from flask_socketio import emit
from backend.Board import *
from backend.Player import *
from backend.Character import *

# we will add all the events onto this object, then import
# this in init
from .extensions import socketio

# This will base the events on database
from .sql import *
import pymysql
from client.dbAccount import*

db = pymysql.connect(host='localhost', port=3306, user=usr, password=pwd, db='NotAClue', charset='utf8')
board = Gameboard()

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

    # set the characterId field and position field for the player object
    # note that we assume that <<<<<<<request.id==player.id>>>>>>>>
    player_id=request.sid
    player_object=Player.getInstanceById(player_id)

    character_object=Character(None,character,"icon")
    
    roomName=character_object.location
    room_object=Room.getInstanceByName(roomName)

    if(player_object == None):
        player_object = Player(player_id, character_object.id, character, username, room_object.id, room_object, 0)

    else:
        player_object.characterId=character_object.id
        player_object.roomId=room_object.id
        player_object.room = room_object



# This function starts the game!
@socketio.on("game_start")
def handle_game_start():    
    emit("start_game", broadcast=True)
    
# Determines where the user clicked and returns the room
@socketio.on("room_select")
def room_selected(x, y):
    location = board.determine_html_location(x, y)
    if location == None:
        ValueError("Choose a room, hallway, or secret passage please")
    else:
        handle_player_room_choose(location)


@socketio.on("character")
def handle_character(character):
    emit("character", character, broadcast=True)

@socketio.on("SID")
def changeSid():
    Player.instances_database[Player.instances_count - 1].id = request.sid

# Handles when a player chooses a room
# TODO: Get current player and make function def handle_player_room_choose(player: Player, newRoomId)
def handle_player_room_choose(room: str):
    player = Player.getInstanceById(request.sid)
    currRoom = board.get_room_by_id(player.room.id)
    newRoom = board.get_room_by_name(room)
    if(currRoom.name in board.rooms):
        newRoomChoices = board.layout[currRoom]
    elif (currRoom.name in board.hallways):
        newRoomChoices = board.hallLayout[currRoom]
    if(newRoom in newRoomChoices):
        player.move(newRoom)
    else:
        raise ValueError("You must choose a location that is adjacent to you (unless you can take a secret passage)")
