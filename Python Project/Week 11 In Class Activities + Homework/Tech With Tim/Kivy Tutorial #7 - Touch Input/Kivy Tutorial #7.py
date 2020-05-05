import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):    # Overwrite and changing the functionality

    btn = ObjectProperty(None)

    def on_touch_down(self, touch): # Once pressed, get position on the screen
        print('Mouse Down', touch)
        self.btn.opacity = 0.5
    def on_touch_move(self, touch): # Once moved, ...
        print('Mouse Move', touch)
    def on_touch_up(self, touch):
        print('Mouse Up', touch)
        self.btn.opacity = 1

class MyApp(App): # Create my.kv, remove the app
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()