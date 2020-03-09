# 1. No Braces / Semicolons
# 2. Line endings / Indentation
# 3. Everything is an object

print('Hello World') # Print Function
# - Comments, runs at the end of the line
# To run script - python file.py

import platform #Import lib
print('This is python version {}".format(platform.python_version()))

import platform

def main(): # Calls main function

def message():
	print('This is the message') # Indentation

if __name__ == '__main__': main()


x = y # Assignment
x * y # Operation
(x, y ) # Tuple
x # Built-in simple value
True # Built-in constant value
f() # Function call

### Print Function ###
print()

print('Hello World') # Prints 'Hello World'

x = 42
print('Hello {}'.format(x)) # Print 'Hello 42', the format is method of the string object
print(f'Hello {x}) #Same as above

# Controls
# If - Else statement
if x < y:
	print(x)
elif x > y:
	print(y)
else:
	print('same')
	
# Loops
x = 0 # Init statement
while x < 10:	# Check if condition is true
	print(x)
	x += 1	# Increment
	
for i in range(10): # Runs fr 1 - 9
	print(x)

def function(n): # Declares a function
	print(n)
function(12)	# Calls function

def function(n):
	return n		# Returns arguments

x = function(12)	# Runs in function, argument = 12
print(x)			# Prints value


class Duck:	# Class
	sound = 'quack quack'	# Instantiation of class, object
	movement = 'swish swish'
	
class Duck:
	def __init__(self, sound, movement):	# Class Constructor, self - reference to object
		self._sound = sound
		self._movement = movement
	
	def sound():
		print('Quack')
	
	def movement():
		print('Swish swish')
	
def main():		# Calling object
	donald = Duck()
	donald.sound()
	donald.movement()

if __name__ = '__main__': main()