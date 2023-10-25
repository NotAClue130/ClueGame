# This run function follows the tutorial: https://www.youtube.com/watch?v=AMp6hlA8xKA

# first import our game from the clueless package

#from clueLess import create_app, socketio

from client import create_app, socketio
from dbAccount import*

# This will base the events on database
from client.sql import *
import pymysql

# first connect to the database
db = pymysql.connect(host='localhost', port=3306, user=usr, password=pwd, db='NotAClue', charset='utf8')

SQL_refresh_database(db)


# then create the app
app = create_app()

# run the game!
socketio.run(app, host=('0.0.0.0'))

