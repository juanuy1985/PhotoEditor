import sys

class Image:
    def __init__(self):

        self.type = 0
        self.size = 0
        self.reservedField1 = 0
        self.reservedField2 = 0
        self.offset = 0
        self.size2 = 0
        self.width = 0
        self.height = 0
        self.planes = 0
        self.bitCount = 0
        self.compression = 0
        self.sizeImage = 0
        self.xPixelsPerMeter = 0
        self.yPixelsPerMeter = 0
        self.colorUsed = 0
        self.colorImportant = 0
        self.extraBytes = 0
        self.dataImage = None


    def getPixel(self, x, y):
        pass