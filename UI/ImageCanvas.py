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

class ImageCanvas(Widget):
    def __init__(self, fileName, **args):
        super(ImageCanvas, self).__init__(**args)
        
        """wavelet = getWavelet(self.fileName, 1)
        wavelet.convert('RGB').save(fileProcessed)
        """
        reader = ReaderBMP()
        image = reader.load(fileName)

        width = image.width
        height = image.height
        texture = Texture.create(size=(width, height))
        texture.blit_buffer(image.dataImage, colorfmt='rgb', bufferfmt='ubyte')

        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=self.size)
        pass