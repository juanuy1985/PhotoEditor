import PIL
from PIL import Image

def getProfile(fileName):
    img = Image.open(fileName)
    img1 = Image.open(fileName)
    width, height = img.size
    image = img.convert('RGB')
    image1 = img.convert('RGB')

    mask = [
        [-1, -1, -1],
        [-1, +9, -1],
        [-1, -1, -1]
    ]

    for x in range(1, width-1):
        for y in range(1, height-1):
            (r, g, b) = (0, 0, 0)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel = image.getpixel((x+i, y+j))
                    r += pixel[0] * mask[i+1][j+1]
                    g += pixel[1] * mask[i+1][j+1]
                    b += pixel[2] * mask[i+1][j+1]
            image1.putpixel((x, y), (r, g, b))
    return image1