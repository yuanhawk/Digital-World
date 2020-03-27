import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase
from libdw import pyrebase
projectid = "wk4firebase-8bcb1"
url = "https://wk4firebase-8bcb1.firebaseio.com/"
authdomain = "wk4firebase-8bcb1.firebaseapp.com"
apikey = "AIzaSyBio92QNkX3uonHzXA5GKKKzzKon9EJeZo"
email = "liyuan_tan@mymail.sutd.edu.sg"
password = "123456" 

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": url,
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)
# Use GPIO12, 16, 20 and 21 for the buttons.
# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.
lst = [25,16,20,21]
for n in lst:
    GPIO.setup(n,GPIO.IN,GPIO.PUD_DOWN)
# Keep a list of the expected movements that the eBot should perform sequentially.
movement_list = []
done = False
buttons = {'left':25,'up':16,'right':20}

while True:
    
    for key in buttons:
        
        if GPIO.input(buttons[key]) == GPIO.HIGH:
            print("button pressed", key)
            movement_list.append(key)
            print(movement_list)
            sleep(0.2)
        if GPIO.input(21) == GPIO.HIGH:
            print(GPIO.input(21))
            done = True
            db.child('rasppy').set(movement_list, user['idToken'])
            print('exiting')
            movement_list = []
