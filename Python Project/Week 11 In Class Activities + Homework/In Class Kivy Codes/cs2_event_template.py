from kivy.app import App
from kivy.uix.label import Label


class SlideDetectApp(App):
    def build(self):
        # building widgets
        # return root widget
        lbl_slide = Label(text='Slide Me', font_size=72, on_touch_move=self.detect)
        # lbl_slide.bind(on_touch_move=self.detect)
        return lbl_slide

    def detect(self, instance, touch):
        # if not instance.collide_point(touch.x, touch.y):
        #   return False
        print(touch.x, touch.y)
        # touch gives touch information

        if touch.dx < -40:
            instance.text = 'Slide Left'
        if touch.dx > 40:
            instance.text = 'Slide Right'
        if touch.dy < -40:
            instance.text = 'Slide Down'
        if touch.dy > 40:
            instance.text = 'Slide Up'
        return True

if __name__=="__main__":
    # when you type in termina;
    # python cs2_event_template.py
    SlideDetectApp().run()
