import PIL
from PIL import Image

def getProjection(fileName):
    img = Image.open(fileName)
    img1 = Image.open(fileName)
    width, height = img.size
    image = img.convert('RGB')
    image1 = img.convert('RGB')

    P = [
        [0.6, .5, 0],
        [.15, 0.6, 0],
        [0, 0, 1]
    ]

    a11 = P[0][0]
    a12 = P[0][1]
    b1 = P[0][2]
    a21 = P[1][0]
    a22 = P[1][1]
    b2 = P[1][2]
    c1  = P[2][0]
    c2  = P[2][1]

    for x in range(width):
        for y in range(height):
            image1.putpixel((x, y), (0, 0, 0))

    for x in range(width):
        for y in range(height):
            newX = ( a11 * x + a12 * y + b1 ) / (c1 * x + c2 * y + 1)
            newY = ( a21 * x + a22 * y + b2 ) / (c1 * x + c2 * y + 1)
            newX = 0 if newX < 0 else newX
            newY = 0 if newY < 0 else newY
            newX = width-1 if newX >= width else newX
            newY = height-1 if newY >= height else newY
            image1.putpixel((int(newX), int(newY)), image.getpixel((x, y)))
    return image1