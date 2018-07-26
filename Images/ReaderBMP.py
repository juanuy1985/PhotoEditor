import struct
from Images.Reader import Reader
from Images.Image import Image

class ReaderBMP(Reader):
    def __init__(self):
        super()
        pass

    def __Word__(self, file):
        return struct.unpack('H', file.read(2))[0]

    def __Dword__(self, file):
        return struct.unpack('i', file.read(4))[0]

    def load(self, path):
        image = Image()
        
        with open(path, "rb") as file:
            image.type = self.__Word__(file)
            image.size = self.__Dword__(file)
            image.reservedField1 = self.__Word__(file)
            image.reservedField2 = self.__Word__(file)
            image.offset = self.__Dword__(file)

            if image.type == 19778:
                image.size2 = self.__Dword__(file)
                image.width = self.__Dword__(file)
                image.height = self.__Dword__(file)
                image.planes = self.__Word__(file)
                image.bitCount = self.__Word__(file)
                image.compression = self.__Dword__(file)
                image.sizeImage = self.__Dword__(file)
                image.xPixelsPerMeter = self.__Dword__(file) 
                image.yPixelsPerMeter = self.__Dword__(file) 
                image.colorUsed = self.__Dword__(file)
                image.colorImportant = self.__Dword__(file)

                file.seek(image.offset)

                image.dataImage = file.read(image.sizeImage)
                image.extraBytes = (image.sizeImage - image.width * image.height * 3) / image.height
            else:
                raise Exception('Exception: {0} - format file incorrect - {1}'.format(path, image.type))
            
        return image
        
        pass