from kivy.metrics import sp
from kivy.core.window import Window
from kivy.app import App
from kivy.clock import Clock
from kivy import properties as kp
from kivy.uix.widget import Widget
from kivy.animation import Animation

from collections import defaultdict # dictionary called with empty key, it creates it instead of returning an error
from random import randint

# global variables
SPRITE_SIZE = sp(20) # squares, scale the pixels, look of the same ratio
COLS = int(Window.width/SPRITE_SIZE) # How many sprites can fit inside the window
ROWS = int(Window.height/SPRITE_SIZE)

LENGTH = 4
MOVESPEED = .1

ALPHA =.5

LEFT = 'left'
UP = 'up'
RIGHT = 'right'
DOWN = 'down'

direction_values = {LEFT: [-1,0], UP: [0,1], RIGHT: [1,0], DOWN: [0,-1]} # direction using a dictionary

direction_group = {LEFT: 'horizontal', UP: 'vertical', RIGHT: 'horizontal', DOWN: 'vertical'}

direction_keys = {'a': LEFT, 'w': UP, 'd': RIGHT, 's': DOWN} # Assign letters to directions

class Sprite(Widget):
    coord = kp.ListProperty([0,0])
    bgcolor = kp.ListProperty([0,0,0,0])

SPRITES = defaultdict(lambda: Sprite()) # Default dictiontary that takes in a function that creates a new instance that I want

class Fruit(Sprite):
    pass

class SnakeApp(App):
    sprite_size = kp.NumericProperty(SPRITE_SIZE) # Keep track of sprite_size

    head = kp.ListProperty([0,0]) # Coordinates, keep track of where the head
    snake = kp.ListProperty() # Draw the snake
    length = kp.NumericProperty(LENGTH) # Limit to length of snake

    fruit = kp.ListProperty([0,0]) # Coordinates
    fruit_sprite = kp.ObjectProperty(Fruit)

    direction = kp.StringProperty(RIGHT, options=(LEFT, UP, RIGHT, DOWN)) # keep track of direction using property
    buffer_direction = kp.StringProperty(RIGHT, options=(LEFT, UP, RIGHT, DOWN, '')) # takes an empty string
    block_input = kp.BooleanProperty(False) # Change loc once per turn, blocks input once direction has been changed

    alpha = kp.NumericProperty(0)

    def on_start(self): # Event Loop
        self.fruit_sprite = Fruit() # Create fruit on start
        self.fruit = self.new_fruit_location # Make fruit appear in random pos
        self.head = self.new_head_location # Make snake appear in random pos
        Clock.schedule_interval(self.move, MOVESPEED)
        Window.bind(on_keyboard=self.key_handler) # Bind on keyboard events

    def on_fruit(self, *args):
        self.fruit_sprite.coord = self.fruit # the coord of new fruit sprite is the fruit loc
        if not self.fruit_sprite.parent: # Make sure fruit is in canvas
            self.root.add_widget(self.fruit_sprite)

    def key_handler(self, _, __, ___, key, *____):
        try:
            self.try_change_direction(direction_keys[key]) # Check if direction is available
        except KeyError: # Ignores all other errors
            pass

    def try_change_direction(self, new_direction):
        if direction_group[new_direction] != direction_group[self.direction]: # Does not allow translocation in vertical, horizontal.
            if self.block_input: # if input is blocked, change the direction once per turn, but if clicked another time, it would change direction automatically
                self.buffer_direction = new_direction # buffer new direction
            else:
                self.direction = new_direction
                self.block_input = True # Block input

    def on_head(self, *args): # kivy property changes, starts with on_<function>
        self.snake.append(self.head) # Append pos of the head in the snake list
        self.snake = self.snake[-self.length:] + [self.head] # list comprehension of the snake, retrieve the reverse indexes, last 4 len loc + head loc

    @property
    def new_head_location(self): # Returns new head loc within bound
        return [randint(2, dim - 2) for dim in [COLS, ROWS]]

    @property
    def new_fruit_location(self):
        while True:
           fruit = [randint(0, dim - 1) for dim in [COLS, ROWS]]
           if fruit not in self.snake and fruit != self.fruit: # Check if fruit is in snake, whether fruit is on the same pos
                return fruit

    def on_snake(self, *args): # if snake changes according to head appended
        for index, coord in enumerate(self.snake): # index,tuple
            sprite = SPRITES[index] # make a sprite widget if I need 1
            sprite.coord = coord # sprite obj created even tho the index does not exist
            if not sprite.parent: # if sprite does not have the parent
                self.root.add_widget(sprite) # add sprite

    def move(self, *args): # Takes in clock event, when snake moves, head moves in another direction
        self.block_input = False # Unblock everytime it is moved
        new_head = [sum(x) for x in zip(self.head, direction_values[self.direction])] # obtain new pos of head using list comprehension, sum self.head + value of current self.direction, return tuple using zip
        if not self.check_in_bounds((new_head)) or new_head in self.snake: # check if not in bounds, or new_head crashes with snake
            return self.die()
        if new_head == self.fruit: # if head collides with fruit
            self.length += 1
            self.fruit = self.new_fruit_location # spawn fruit in new loc
        if self.buffer_direction: # change direction once snake moves
            self.try_change_direction(self.buffer_direction)
            self.buffer_direction = '' # Buffer direction is none
        self.head = new_head # move the head around

    def check_in_bounds(self, pos):
        return all(0 <= pos[x] < dim for x, dim in enumerate([COLS, ROWS])) # if pos within bound

    def die(self):
        self.root.clear_widgets() # clear widgets
        self.alpha = ALPHA # move ALPHA(0.5 -> 0)
        Animation(alpha=0, duration=MOVESPEED).start(self) # Create animation
        self.snake.clear() # Reset state of snake
        self.length = LENGTH # Reset length

        self.fruit = self.new_fruit_location # sets new fruit location
        self.head = self.new_head_location # sets new head position

if __name__ == '__main__':
    sa = SnakeApp()
    sa.run()