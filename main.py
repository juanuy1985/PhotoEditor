import sys

from Images.Image import Image
from Images.ReaderBMP import ReaderBMP

def main(argv):
    print("Esto es una prueba")
    
    reader = ReaderBMP()

    image = reader.load("D:\Maestría\CG\Briggi\MostrarBMP\Pruebas\Fatima.bmp")


    
    pass

if __name__ == "__main__":
    main(sys.argv)