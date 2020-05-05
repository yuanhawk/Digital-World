from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock # Use clock object to schedule things by frame
from kivy.core.audio import SoundLoader

def collides(rect1, rect2): # Objects are rectangles and not rotating, tuple / axis-aligned bounding box
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect1[1][1]
    if r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y:
        return True
    else:
        return False

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # Overriding init method, call super initialise base classes
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self) # init keyboard object
        self._keyboard.bind(on_key_down=self._on_key_down) # event listener, call back
        self._keyboard.bind(on_key_up=self._on_key_up)

        with self.canvas:
            self.player = Rectangle(pos=(0,0), size=(100,100)) # use source to link image files
            self.enemy = Rectangle(pos=(400,400), size=(80,80))

        self.keysPressed = set()

        Clock.schedule_interval(self.move_step, 0) # Do every frame

        self.sound = SoundLoader.load('error-remix.wav')
        self.sound.play()

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(text) # Every time key pressed it is added to the set

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    def move_step(self, dt):
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        step_size = 200 * dt # 100px per sec (frame rate movement)

        if 'w' in self.keysPressed:
            currenty += 1
        if 's' in self.keysPressed:
            currenty -= 1
        if 'a' in self.keysPressed:
            currentx -= 1
        if 'd' in self.keysPressed:
            currentx += 1
        self.player.pos = (currentx, currenty)

        if collides((self.player.pos, self.player.size), (self.enemy.pos, self.enemy.size)):
            print('colliding')
        else:
            print('not colliding')

class MyApp(App):
    def build(self):
        return GameWidget() # Widget is base class for GUI elements

if __name__ == '__main__':
    MyApp().run()