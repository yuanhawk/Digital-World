#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythymiodw import *

def print_temp(t_celsius):
	t_fahrenheit = ( t_celsius * 9 / 5 ) + 32
	t_fahrenheit_s = '{:.3f}'.format(t_fahrenheit)
	return t_fahrenheit_s

def forward(speed, duration):
	robot.wheels(speed, speed)
	robot.sleep(duration)

robot = ThymioReal() # create an object

############### Start writing your code here ################ 

# Prompt user to enter speed and duration of movement
speed = float(input("Enter the speed of the movement in mm/s: "))
duration = int(input("Enter the duration of the movement in s: "))

# Move according to the specified speed and duration
forward(speed, duration)


# Read temperature in celcius from the sensor and print it
t_celsius = robot.temperature
t_celsius_s = '{:.3f}'.format(t_celsius)
print("The temperature is ", t_celsius_s, " degree Celsius and", print_temp(t_celsius), " degree Fahrenheit")
########################## end ############################## 

robot.quit() # disconnect the communication

#prompt the user to input the forward throttle value for both wheels and duration to move forward.
#Both of these values are passed as arguments to a function called forward which does not return
#any value.
#This function moves the robot forward for x number of seconds using
#these values. For example, if the input values are 70 and 3, the robot will move
#forward with speed of 70 on both wheels for 3 seconds. The maximum number for
#speed is 500, which is equivalent to about 20 cm/s.
