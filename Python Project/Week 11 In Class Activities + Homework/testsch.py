import kivy
from kivy.app import App
from kivy.uix.label import Label
# (1) subclassing the "App" class
class MyApp(App):
# (2) implement its "build" method
    def build(self):
    	# (3) make it return a "Widget" instance
    	return Label(text='Hello world')
MyApp().run()