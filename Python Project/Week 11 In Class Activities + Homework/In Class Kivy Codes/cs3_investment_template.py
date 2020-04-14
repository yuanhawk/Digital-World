from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 


class MyLabel(Label):

    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs) # Creating your own label
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)
        self.font_size = 24
        self.halign = 'left'
        self.valign = 'middle'

class MyInput(TextInput):

    def __init__(self, **kwargs): # Gives infinite numbers of variables
        # TextInput.__init__(self, **kwargs)
        super().__init__(**kwargs)
        self.font_size = 24
        self.multiline = False

class Investment(App):

    def build(self):
        layout = GridLayout(cols=2)
        #halign - > Horizontal alignment, valign -> Vertical alignment
        # Label 1
        l1 = MyLabel(text="Investment Ammount")
        layout.add_widget(l1)
        # Text 1
        self.t1 = MyInput(text="0.0")
        layout.add_widget(self.t1)

        # Label 2
        l2 = MyLabel(text="Years")
        layout.add_widget(l2)
        # Text 2
        self.t2 = MyInput(text="0.0")
        layout.add_widget(self.t2)

        # Label 3
        l3 = MyLabel(text="Annual Interest Rate")
        layout.add_widget(l3)
        # Text 3
        self.t3 = MyInput(text="0.0")
        layout.add_widget(self.t3)

        # Label 4
        l4 = MyLabel(text="Future Value")
        layout.add_widget(l4)

        # Label 5
        self.lbl_output = MyLabel(text="")
        layout.add_widget(self.lbl_output)

        btn = Button(text="Calculate", on_press=self.calculate, font_size=24)
        layout.add_widget(btn)
        return layout

    def calculate(self, instance):
        inv_amt = float(self.t1.text) # Using text input
        years = float(self.t2.text)
        mth_int_rate = float(self.t3.text) / 100 / 12
        txt_future_val = inv_amt * (1 + mth_int_rate)**(years * 12)
        self.lbl_output.text = "{:.2f}".format(txt_future_val)


Investment().run()
