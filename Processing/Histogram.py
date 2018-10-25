import PIL
from PIL import Image
import numpy as np

def getHistogram(fileName):
    img = Image.open(fileName)
    width, height = img.size
    image = img.convert('RGB')
    gray = np.zeros((width, height))
    for x in range(0, width):
        for y in range(0, height):
            (r, g, b) = image.getpixel((x, y))
            gray[x, y] = np.floor(0.3 * r + 0.59 * g + 0.11 * b)

    histograma = np.zeros(256)
    for x in range(0, width):
        for y in range(0, height):
            index = int(gray[x, y])
            histograma[index] += 1

    for index in range(1, 256):
        histograma[index] += histograma[index-1] 

    accumMinimum = histograma[0]
    lookUp = np.zeros((256))
    
    for index in range(256):
        lookUp[index] = np.floor(255 * (histograma[index] - accumMinimum) / (height * width - accumMinimum) )
	
    for x in range(0, width):
        for y in range(0, height):
            tmp = int(lookUp[int(gray[x, y])])
            image.putpixel((x, y), (tmp, tmp, tmp))

    return image