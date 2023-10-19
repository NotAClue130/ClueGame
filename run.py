# This run function follows the tutorial: https://www.youtube.com/watch?v=AMp6hlA8xKA

# first import our game from the clueless package

from clueLess import create_app, socketio

from client import create_app, socketio


# then create the app
app = create_app()

# run the game!
socketio.run(app, host=('0.0.0.0'))

socketio.run(app, host=('0.0.0.0'), port=4000)

