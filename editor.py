from itertools import chain
import six
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture


class MyWidget(Widget):
    def __init__(self, **args):
        super(MyWidget, self).__init__(**args)
        width = 640
        height = 480
        # create a 64x64 texture, defaults to rgba / ubyte
        texture = Texture.create(size=(width, height))

        # create 64x64 rgb tab, and fill with values from 0 to 255
        # we'll have a gradient from black to white
        size = width * height * 3
        buf = [int(x * 255 / size) for x in range(size)]

        # then, convert the array to a ubyte string
        #buf = b''.join(map(chr, buf))
        buf = b''.join(list(map(lambda x: six.int2byte(x), buf)))

        # then blit the buffer
        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

        # that's all ! you can use it in your graphics now :)
        # if self is a widget, you can do this
        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=(width, height))


class TestApp(App):
    def build(self):
        return MyWidget(size=(368, 512))


if __name__ == '__main__':
    TestApp().run()
