from itertools import chain
import six
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture
from Images.Image import Image
from Images.ReaderBMP import ReaderBMP
from skimage import data, io, filters
from Processing.Wavelet import getWavelet
from kivy.core.window import Window
import os.path

class ImageCanvasWavelet(Widget):

    def __init__(self, **args):
        super(ImageCanvasWavelet, self).__init__(**args)
        self._fileName = ''
        self._scales = 0

    def get_fileName(self):
        return self._fileName

    def set_fileName(self, value):
        self._fileName = value
        self.process()
        
    def get_scales(self):
        return self._scales

    def set_scales(self, value):
        self._scales = value
        self.process()

    def process(self):
        self.canvas.clear()

        if os.path.isfile(self.fileName) :    
            reader = ReaderBMP()
            image = reader.load(self.fileName)

            processedFile = self.fileName.replace('.bmp', '_processed.bmp')
            self.processWavelet(self.fileName, processedFile)

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

    def processWavelet(self, fileName, processedFileName):
        wavelet = getWavelet(fileName, int(self.scales))
        wavelet.convert('RGB').save(processedFileName)

    fileName = property(get_fileName, set_fileName)

    scales = property(get_scales, set_scales)
    
