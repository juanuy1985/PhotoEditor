from itertools import chain
import six
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture
from Images.Image import Image
from Images.ReaderBMP import ReaderBMP

class ImageCanvas(Widget):
    def __init__(self, **args):
        super(ImageCanvas, self).__init__(**args)

        reader = ReaderBMP()
        image = reader.load("D:\Maestría\CG\Juan\Pruebas\DragonBall.bmp")

        width = image.width
        height = image.height
        texture = Texture.create(size=(width, height))
        size = width * height * 3
        texture.blit_buffer(image.dataImage, colorfmt='rgb', bufferfmt='ubyte')

        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=(width, height))
        pass