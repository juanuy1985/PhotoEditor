import PIL
from PIL import Image

def getMedian(fileName):
    img = Image.open(fileName)
    img1 = Image.open(fileName)
    width, height = img.size
    image = img.convert('RGB')
    image1 = img.convert('RGB')

    for x in range(1, width-1):
        for y in range(1, height-1):
            neighbourhood = [
                image.getpixel((x-1, y-1)), image.getpixel((x, y-1)), image.getpixel((x+1, y-1)),
                image.getpixel((x-1, y)), image.getpixel((x, y)), image.getpixel((x+1, y)),
                image.getpixel((x-1, y+1)), image.getpixel((x, y+1)), image.getpixel((x+1, y+1))
            ]
            neighbourhood.sort(key=lambda color: color[0])
            r = neighbourhood[4][0]
            neighbourhood.sort(key=lambda color: color[1])
            g = neighbourhood[4][1]
            neighbourhood.sort(key=lambda color: color[2])
            b = neighbourhood[4][2]
            image1.putpixel((x, y+1), (r, g, b))
    return image1