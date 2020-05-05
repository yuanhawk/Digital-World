from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image

#from kivy.utils import get_color_from_hex
#green = get_color_from_hex('#______')
#Color(*green)


class Game(Widget): # 100 * 100 px, draw in canvas, handle user input
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source='images/background.png'))

class GameApp(App):
    def build(self):
        return Game(size=Window.size)

if __name__ == '__main__':
    GameApp().run()