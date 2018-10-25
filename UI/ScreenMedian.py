from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

class ScreenMedian(Screen):
    def build(self):
        button = Button(text='Hola doc soy wavelet')
        return button