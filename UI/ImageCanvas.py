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
        # create a 64x64 texture, defaults to rgba / ubyte
        texture = Texture.create(size=(width, height))

        # create 64x64 rgb tab, and fill with values from 0 to 255
        # we'll have a gradient from black to white
        size = width * height * 3
        
        # then blit the buffer
        texture.blit_buffer(image.dataImage, colorfmt='rgb', bufferfmt='ubyte')

        # that's all ! you can use it in your graphics now :)
        # if self is a widget, you can do this
        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=(width, height))
        pass