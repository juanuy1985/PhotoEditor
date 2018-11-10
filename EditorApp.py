from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from UI.ScreenWavelet import ScreenWavelet
from UI.ScreenMedian import ScreenMedian
from UI.ScreenHistograma import ScreenHistograma
from UI.ScreenPerfilado import ScreenPerfilado
from UI.ScreenSmooth import ScreenSmooth
from UI.ScreenProjection import ScreenProjection
from UI.ScreenBilineal import ScreenBilineal
from kivy.uix.textinput import TextInput
from UI.ImageCanvasWavelet import ImageCanvasWavelet
from UI.ImageCanvasMedian import ImageCanvasMedian
from UI.ImageCanvasHistograma import ImageCanvasHistograma
from UI.ImageCanvasPerfilado import ImageCanvasPerfilado
from UI.ImageCanvasSmooth import ImageCanvasSmooth
from UI.ImageCanvasProjection import ImageCanvasProjection
from UI.ImageCanvasBilineal import ImageCanvasBilineal

class Display(BoxLayout):
    pass

class EditorApp(App):
    def build(self):
        return Display()

    