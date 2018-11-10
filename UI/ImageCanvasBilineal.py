from itertools import chain
import six
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture
from Images.Image import Image
from Images.ReaderBMP import ReaderBMP
from skimage import data, io, filters
from Processing.Bilineal import getBilineal
from kivy.core.window import Window
import os.path

class ImageCanvasBilineal(Widget):

    def __init__(self, **args):
        super(ImageCanvasBilineal, self).__init__(**args)
        self._fileName = ''

    def get_fileName(self):
        return self._fileName

    def set_fileName(self, value):
        self._fileName = value
        self.process()
        
    def process(self):
        self.canvas.clear()

        if os.path.isfile(self.fileName) :    
            reader = ReaderBMP()
            image = reader.load(self.fileName)

            processedFile = self.fileName.replace('.bmp', '_processedSmooth.bmp')
            self.processBilineal(self.fileName, processedFile)

            imageProcessed = reader.load(processedFile)

            width = image.width 
            height = image.height
            texture = Texture.create(size=(width, height))
            texture.blit_buffer(image.dataImage, colorfmt='rgb', bufferfmt='ubyte')

            texture1 = Texture.create(size=(width, height))
            texture1.blit_buffer(imageProcessed.dataImage, colorfmt='rgb', bufferfmt='ubyte')
            size = Window.width/2*0.8

            with self.canvas:
                Rectangle(texture=texture, pos=(0,0), size=(size, size))
                Rectangle(texture=texture1, pos=(Window.width-size,0), size=(size, size))
        pass

    def processBilineal(self, fileName, processedFileName):
        profiled = getBilineal(fileName)
        profiled.save(processedFileName)

    fileName = property(get_fileName, set_fileName)

