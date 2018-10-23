from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from UI.ImageCanvas import ImageCanvas
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionButton
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionPrevious 
from Processing.Wavelet import getWavelet

class EditorApp(App):
    def build(self):
        self.title = "Photo Editor - powered by Juanuy"
        #Window.maximize()
        Window.clearcolor = (1, 1, 1, 1)
        
        root = BoxLayout(orientation = 'vertical',size_hint=(100, None), height = Window.height+110)
        root.add_widget(self.createMainMenu())

        w = Window.width
        h = Window.height

        fileName = "D:\\Maestria\\CG\\Juan\\Pruebas\\The Nun.bmp"
        processedFileName = "D:\\Maestria\\CG\\Juan\\Pruebas\\The Nun_Processed.bmp"

        self.processWavelet(fileName, processedFileName)

        canvas1 = ImageCanvas(fileName = fileName, size=(8*w/20, 5*h/8), pos=(w/15, h/4))
        canvas2 = ImageCanvas(fileName = processedFileName, size=(8*w/20, 5*h/8), pos=(8*w/15, h/4)) 

        root.add_widget(canvas1)
        root.add_widget(canvas2)
        return root
    pass

    def createMainMenu(self):
        actionBar = ActionBar(pos_hint={'top': 1.0})
        actionButton = ActionButton()
        actionPrevious = ActionPrevious(title='', with_previous=False)
        actionView = ActionView()
        actionView.add_widget(actionButton)
        actionView.add_widget(actionPrevious)
        actionBar.add_widget(actionView)
         
        return actionBar
    
    #Esta demostracion es para la maestria de CS de la UNSA
    #Juan Vilca Castro
    #Prof: Juan Carlos Gutierrez
    def processWavelet(self, fileName, processedFileName):
        wavelet = getWavelet(fileName, 4)
        wavelet.convert('RGB').save(processedFileName)