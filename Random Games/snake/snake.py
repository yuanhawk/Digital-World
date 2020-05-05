from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

from random import randint

class SnakePart(Widget):
    pass

class GameScreen(Widget):
    step_size = 40 # Movement per frame
    movement_x = 0
    movement_y = 0
    snake_parts = []
    def new_game(self):
        to_be_removed = []
        for child in self.children: # clear any widget
            if isinstance(child, SnakePart): # check if child is snakepart
                to_be_removed.append(child)
        for child in to_be_removed:
            self.remove_widget(child)

        self.snake_parts = []
        self.movement_x = 0 # snake movement x
        self.movement_y = 0 # snake movement y
        head = SnakePart()
        head.pos = (0,0)
        self.snake_parts.append(head)
        self.add_widget(head)

    def on_touch_up(self, touch):
        dx = touch.x - touch.opos[0] # Slide screen
        dy = touch.y - touch.opos[1]
        if abs(dx) > abs(dy):
            # Moving left or right
            self.movement_y = 0
            if dx > 0: # Moving right
                self.movement_x = self.step_size
            else: # moving left
                self.movement_x = - self.step_size
        else:
            # Moving up or down
            self.movement_x = 0
            if dy > 0:
                self.movement_y = self.step_size
            else:
                self.movement_y = - self.step_size

    def collides_widget(self, wid1, wid2):
        if wid1.right <= wid2.x:
            return False
        if wid1.x >= wid2.right:
            return False
        if wid1.top <= wid2.y:
            return False
        if wid1.y >= wid2.top:
            return False
        return True

    def next_frame(self, *args):
        # Move the snake
        # Move the head
        head = self.snake_parts[0]
        food = self.ids.food
        last_x = self.snake_parts[-1].x # Get last snake part x value
        last_y = self.snake_parts[-1].y # Get last snake part y value

        # Move the body
        for i, part in enumerate(self.snake_parts):
            if i == 0: # Head
                continue
            part.new_y = self.snake_parts[i-1].y # Get previous snake part y
            part.new_x = self.snake_parts[i-1].x # Get previous snake part x
        for part in self.snake_parts[1:]: # except the head
            part.y = part.new_y
            part.x = part.new_x

        # Move the head
        head.x += self.movement_x
        head.y += self.movement_y

        # Check for snake colliding with food
        if self.collides_widget(head, food):
            food.x = randint(0, Window.width - food.width) # pos of food is random
            food.y = randint(0, Window.height - food.height) # pos of food is random
            new_part = SnakePart()
            new_part.x = last_x
            new_part.y = last_y
            self.snake_parts.append(new_part)
            self.add_widget(new_part)

        # Check for snake colliding with snake
        for part in self.snake_parts[1:]: # Check each snake part
            if self.collides_widget(part, head):
                self.new_game()

        # Check for snake colliding with wall
        if not self.collides_widget(self, head): # If head is not in GameScreen
            self.new_game()

class Pipe(Widget):
    def __init__(self, pos):
        super().__init__(pos=pos)
        self.top_image = Sprite(source='images/pipe_top.png')
        self.top_image.pos = (self.x, self.y / 3.5 * 24)
        self.add_widget(self.top_image)
        self.bottom_image = Sprite(source='images/pipe_bottom.png')
        self.bottom_image.pos = (self.x, self.y - self.bottom_image.height)
        self.add_widget(self.bottom_image)
        self.width = self.top_image.width

    def update(self):
        self.x -= 2
        self.top_image.x = self.bottom_image.x = self.x
        if self.right < 0:
            self.parent.remove_widget(self)

class SnakeApp(App):
    def on_start(self):
        self.root.new_game()
        Clock.schedule_interval(self.root.next_frame, .25) # Refers to GameScreen
        pass

if __name__ == '__main__':
    sa = SnakeApp()
    sa.run()