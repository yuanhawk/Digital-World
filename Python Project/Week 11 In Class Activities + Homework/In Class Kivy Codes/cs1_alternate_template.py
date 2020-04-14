from kivy.app import App
from kivy.uix.label import Label


class AlternateApp(App):

    text_state = 0

    def build(self):
        # build the widgets
        # return the root widget
        lbl_toggle = Label(text="Programming is Fun.", font_size=72)
        lbl_toggle.bind(on_touch_down=self.alternate) #Event name-on_touch_down, method-self.alternate, not a function call
        return lbl_toggle

    def alternate(self, instance, touch): # method definition
        # instance is the widget that triggers the event
        if self.text_state == 0:
            instance.text = 'It is FUN to program.'
            # self.text_state = 1
        else:
            instance.text = 'Programming is Fun'
            # self.text_state = 0
        self.text_state = 1 - self.text_state


myapp = AlternateApp() # Object instantiation
myapp.run() # Event Loop
