from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from UI.ImageCanvas import ImageCanvas

class EditorApp(App):
    def build(self):
        self.title = "Photo Editor - powered by Juanuy"
        Window.maximize()
        Window.clearcolor = (1, 1, 1, 1)
        
        root = BoxLayout(orientation = 'vertical',size_hint=(1, None), height = Window.height+110)
        root.add_widget(ImageCanvas())
        return root
    pass
