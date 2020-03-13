from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.layout import Layout

class MyLayout(Layout):
    def __init__(self,**karws):
        super(MyLayout,self).__init__(**karws)

class mykv(App):
    pass

mykv().run()
