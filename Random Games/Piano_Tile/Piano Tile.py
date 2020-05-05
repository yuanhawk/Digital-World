from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.properties import OptionProperty, StringProperty
from kivy.clock import Clock
from time import sleep
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.widget import Widget

# Referenced, and adapted from https://youtu.be/U14P8gtjQmU
class Sprite(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = self.texture_size

class Background(Widget):
    def __init__(self, source):
        super().__init__()
        self.image = Sprite(source=source, y=3*self.height)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dup1 = Sprite(source=source, x=self.width, y=.95 * self.height)
        self.add_widget(self.image_dup1)


    def update(self):
        self.image.x -= 2
        self.image_dup1.x -= 2

        if self.image.right <= 0:
            self.image.x = 0
            self.image_dup1.x = self.width


class Piano(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = Background(source='flappy.jpg')
        self.size = self.background.size
        self.add_widget(self.background)
        Clock.schedule_interval(self.update, 1.0/60.0)

    def update(self, *ignore):
        self.background.update()
############################################

class PianoApp(App):

    note = StringProperty(defaultvalue='')
    state = OptionProperty('stop', options=['stop', 'play']) # State Machine: default - 'stop', when pressed - 'on'

    def build(self):
        piano = Piano()
        overall_layout = GridLayout(rows=2)
        layout = GridLayout(cols=25, rows=1)


        btnC = Button(text='C', on_press=Clock.schedule_once(self.press_C, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnC)

        btnC_sharp = Button(text='C#', background_color=(0,0,0,1), on_press=Clock.schedule_once(self.press_C_sharp, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnC_sharp)

        btnD = Button(text='D', on_press=Clock.schedule_once(self.press_D, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnD)

        btnD_sharp = Button(text='D#', background_color=(0,0,0,1), on_press=Clock.schedule_once(self.press_D_sharp, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnD_sharp)

        btnE = Button(text='E', on_press=Clock.schedule_once(self.press_E, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnE)

        btnF = Button(text='F', on_press=Clock.schedule_once(self.press_F, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnF)

        btnF_sharp = Button(text='F#', background_color=(0,0,0,1), on_press=Clock.schedule_once(self.press_F_sharp, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnF_sharp)

        btnG = Button(text='G', on_press=Clock.schedule_once(self.press_G, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnG)

        btnG_sharp = Button(text='G#', background_color=(0,0,0,1), on_press=Clock.schedule_once(self.press_G_sharp, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnG_sharp)

        btnA = Button(text='A', on_press=Clock.schedule_once(self.press_A, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnA)

        btnA_sharp = Button(text='A#', background_color=(0,0,0,1), on_press=Clock.schedule_once(self.press_A_sharp, -2), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnA_sharp)

        btnB = Button(text='B', on_press=Clock.schedule_once(self.press_B, -1), on_release=self.release_note, on_swipe=self.release_note)
        layout.add_widget(btnB)

        btnC2 = Button(text='C2', on_press=Clock.schedule_once(self.press_C2, -2), on_release=self.release_note,
                      on_swipe=self.release_note)
        layout.add_widget(btnC2)

        btnC2_sharp = Button(text='C2#', background_color=(0, 0, 0, 1),
                            on_press=Clock.schedule_once(self.press_C2_sharp, -2), on_release=self.release_note,
                            on_swipe=self.release_note)
        layout.add_widget(btnC2_sharp)

        btnD2 = Button(text='D2', on_press=Clock.schedule_once(self.press_D2, -2), on_release=self.release_note,
                      on_swipe=self.release_note)
        layout.add_widget(btnD2)

        btnD2_sharp = Button(text='D2#', background_color=(0, 0, 0, 1),
                            on_press=Clock.schedule_once(self.press_D2_sharp, -2), on_release=self.release_note,
                            on_swipe=self.release_note)
        layout.add_widget(btnD2_sharp)

        btnE2 = Button(text='E2', on_press=Clock.schedule_once(self.press_E2, -2), on_release=self.release_note,
                      on_swipe=self.release_note)
        layout.add_widget(btnE2)

        btnF2 = Button(text='F2', on_press=Clock.schedule_once(self.press_F2, -2), on_release=self.release_note,
                      on_swipe=self.release_note)
        layout.add_widget(btnF2)

        btnF2_sharp = Button(text='F2#', background_color=(0, 0, 0, 1),
                            on_press=Clock.schedule_once(self.press_F2_sharp, -2), on_release=self.release_note,
                            on_swipe=self.release_note)
        layout.add_widget(btnF2_sharp)

        btnG2 = Button(text='G2', on_press=Clock.schedule_once(self.press_G2, -2), on_release=self.release_note,
                      on_swipe=self.release_note)
        layout.add_widget(btnG2)

        btnG2_sharp = Button(text='G2#', background_color=(0, 0, 0, 1),
                            on_press=Clock.schedule_once(self.press_G2_sharp, -2), on_release=self.release_note,
                            on_swipe=self.release_note)
        layout.add_widget(btnG2_sharp)

        btnA2 = Button(text='A2', on_press=Clock.schedule_once(self.press_A2, -2), on_release=self.release_note,
                      on_swipe=self.release_note)
        layout.add_widget(btnA2)

        btnA2_sharp = Button(text='A2#', background_color=(0, 0, 0, 1),
                            on_press=Clock.schedule_once(self.press_A2_sharp, -2), on_release=self.release_note,
                            on_swipe=self.release_note)
        layout.add_widget(btnA2_sharp)

        btnB2 = Button(text='B2', on_press=Clock.schedule_once(self.press_B2, -1), on_release=self.release_note,
                      on_swipe=self.release_note)
        layout.add_widget(btnB2)

        btnC3 = Button(text='C3', on_press=Clock.schedule_once(self.press_C3, -2), on_release=self.release_note,
                      on_swipe=self.release_note)
        layout.add_widget(btnC3)

        overall_layout.add_widget(piano)
        overall_layout.add_widget(layout)
        return overall_layout

    def release_note(self, widget, *args):
        self.state = 'stop'
        if self.state == 'stop':
            self.note = ''
            self.sound.stop()
            self.sound.unload()
            anim = Animation(color=(.482, .373, .376, .8))
            anim += Animation(color=(1, 1, 1, 1))
            anim.start(widget)


    def press_C(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/c.wav')
        if self.state == 'play':
            self.note = 'C'
            self.sound.play()
            sleep(.4)

    def press_C_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/c_sharp.wav')
        if self.state == 'play':
            self.note = 'C#'
            self.sound.play()
            sleep(.4)

    def press_D(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/d.wav')
        if self.state == 'play':
            self.note = 'D'
            self.sound.play()
            sleep(.4)

    def press_D_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/d_sharp.wav')
        if self.state == 'play':
            self.note = 'D#'
            self.sound.play()
            sleep(.4)

    def press_E(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/e.wav')
        if self.state == 'play':
            self.note = 'E'
            self.sound.play()
            sleep(.4)

    def press_F(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/f.wav')
        if self.state == 'play':
            self.note = 'F'
            self.sound.play()
            sleep(.4)

    def press_F_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/f_sharp.wav')
        if self.state == 'play':
            self.note = 'F#'
            self.sound.play()
            sleep(.4)

    def press_G(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/g.wav')
        if self.state == 'play':
            self.note = 'G'
            self.sound.play()
            sleep(.4)

    def press_G_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/g_sharp.wav')
        if self.state == 'play':
            self.note = 'G#'
            self.sound.play()
            sleep(.4)

    def press_A(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/a.wav')
        if self.state == 'play':
            self.note = 'A'
            self.sound.play()
            sleep(.4)

    def press_A_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/a_sharp.wav')
        if self.state == 'play':
            self.note = 'A#'
            self.sound.play()
            sleep(.4)

    def press_B(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/b.wav')
        if self.state == 'play':
            self.note = 'B'
            self.sound.play()
            sleep(.4)

    def press_C2(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/c2.wav')
        if self.state == 'play':
            self.note = 'C2'
            self.sound.play()
            sleep(.4)

    def press_C2_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/c2_sharp.wav')
        if self.state == 'play':
            self.note = 'C2#'
            self.sound.play()
            sleep(.4)

    def press_D2(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/d2.wav')
        if self.state == 'play':
            self.note = 'D2'
            self.sound.play()
            sleep(.4)

    def press_D2_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/d2_sharp.wav')
        if self.state == 'play':
            self.note = 'D2#'
            self.sound.play()
            sleep(.4)

    def press_E2(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/e2.wav')
        if self.state == 'play':
            self.note = 'E2'
            self.sound.play()
            sleep(.4)

    def press_F2(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/f2.wav')
        if self.state == 'play':
            self.note = 'F2'
            self.sound.play()
            sleep(.4)

    def press_F2_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/f2_sharp.wav')
        if self.state == 'play':
            self.note = 'F2#'
            self.sound.play()
            sleep(.4)

    def press_G2(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/g2.wav')
        if self.state == 'play':
            self.note = 'G2'
            self.sound.play()
            sleep(.4)

    def press_G2_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/g2_sharp.wav')
        if self.state == 'play':
            self.note = 'G2#'
            self.sound.play()
            sleep(.4)

    def press_A2(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/a2.wav')
        if self.state == 'play':
            self.note = 'A2'
            self.sound.play()
            sleep(.4)

    def press_A2_sharp(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/a2_sharp.wav')
        if self.state == 'play':
            self.note = 'A2#'
            self.sound.play()
            sleep(.4)

    def press_B2(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/b2.wav')
        if self.state == 'play':
            self.note = 'B2'
            self.sound.play()
            sleep(.4)

    def press_C3(self, value):
        self.state = 'play'
        self.sound = SoundLoader.load('sounds/c3.wav')
        if self.state == 'play':
            self.note = 'C3'
            self.sound.play()
            sleep(.4)

if __name__ == '__main__':
    PianoApp().run()