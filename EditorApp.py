from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from UI.ScreenWavelet import ScreenWavelet
from UI.ScreenMedian import ScreenMedian
from kivy.uix.textinput import TextInput
from UI.ImageCanvasWavelet import ImageCanvasWavelet
from UI.ImageCanvasMedian import ImageCanvasMedian

class Display(BoxLayout):
    pass

class EditorApp(App):
    def build(self):
        return Display()

    