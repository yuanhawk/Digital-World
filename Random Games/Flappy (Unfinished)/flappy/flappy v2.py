from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock


class Sprite(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = self.texture_size

# class Background(Sprite):
#     def update(self):
#         self.x -= 2

class Background(Widget):
    def __init__(self, source):
        super().__init__()
        self.image = Sprite(source=source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source=source, x=self.width)
        self.add_widget(self.image_dupe)

    def update(self):
        self.image.x -= 2
        self.image_dupe.x -= 2

        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width


class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    #     with self.canvas:
    #         Color(.5,.5,1)
    #         Rectangle(pos=(0,0), size=self.size)
    #     self.add_widget(Image(source='images/background.png'))
    #     self.add_widget(Image(source='images/bird.png'))
    #     self.add_widget(Sprite(source='images/background.png'))
    #     self.background = Sprite(source='images/background.png')
        self.background = Background(source='images/background.png')
        self.size = self.background.size
        self.add_widget(self.background)
        self.add_widget(Sprite(source='images/bird.png'))
        Clock.schedule_interval(self.update, 1.0/60.0)

    def update(self, *ignore):
        self.background.update()


class GameApp(App):
    def build(self):
        # return Game(size=Window.size)
        game = Game()
        Window.size = game.size
        return game

GameApp().run()