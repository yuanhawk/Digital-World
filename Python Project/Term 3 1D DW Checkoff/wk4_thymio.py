from pythymiodw import *
from time import sleep
from libdw import pyrebase

import RPi.GPIO as GPIO

projectid = "wk4firebase-8bcb1"
dburl = "https://wk4firebase-8bcb1.firebaseio.com/"
authdomain = "wk4firebase-8bcb1.firebaseapp.com"
apikey = "AIzaSyBio92QNkX3uonHzXA5GKKKzzKon9EJeZo"
email = "liyuan_tan@mymail.sutd.edu.sg"
password = "123456"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

sleep(15)

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()

robot = ThymioReal()  # create a robot object

db = firebase.database()

movement_list = []

no_movements = True

while no_movements:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the robot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here

    movement_list = db.child("rasppy").get(user['idToken'])
    print(movement_list.key(), movement_list.val())
    

    if movement_list.val() != None:
        for move in movement_list.val():
            if move == "left":
                robot.wheels(-100, 100)
                robot.sleep(1)
                robot.wheels(0, 0)
            if move == "up":
                robot.wheels(100, 100)
                robot.sleep(1)
                robot.wheels(0, 0)
            if move == "right":
                robot.wheels(100, -100)
                robot.sleep(1)
                robot.wheels(0, 0)
                
        db.child("rasppy").remove(user['idToken'])
