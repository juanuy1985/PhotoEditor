import PIL
from PIL import Image

def getBilineal(fileName):
    img = Image.open(fileName)
    img1 = Image.open(fileName)
    width, height = img.size
    image = img.convert('RGB')
    image1 = img.convert('RGB')

    P = [
        [ 2.1052631578947367, -1.7543859649122806, 0 ],
		[ -0.5263157894736842, 2.1052631578947367, 0 ],
		[ 0, 0, 1 ]
    ]

    a11 = P[0][0]
    a12 = P[0][1]
    b1 = P[0][2]
    a21 = P[1][0]
    a22 = P[1][1]
    b2 = P[1][2]
    c1  = P[2][0]
    c2  = P[2][1]
    coord = []
    for x in range(width):
        coord.append([0] * height)
        for y in range(height):
            image1.putpixel((x, y), (0, 0, 0))
            coord[x][y] = -1

    for x in range(width):
        for y in range(height):
            newX = ( a11 * x + a12 * y + b1 ) / (c1 * x + c2 * y + 1)
            newY = ( a21 * x + a22 * y + b2 ) / (c1 * x + c2 * y + 1)
            newX = 0 if newX < 0 else newX
            newY = 0 if newY < 0 else newY
            newX = width-1 if newX >= width else newX
            newY = height-1 if newY >= height else newY
            image1.putpixel((int(newX), int(newY)), image.getpixel((x, y)))
            coord[int(newX)][int(newY)] = 1
    
    for y in range(height):
        if coord[0][y] == -1:
            image1.putpixel((0, y), (0, 0, 0))
            coord[0][y] = 1

        if coord[width - 1][y] == -1:
            image1.putpixel((width-1, y), (0, 0, 0))
            coord[width - 1][y] = 1

    for x in range(width):
        if coord[x][0] == -1:
            image1.putpixel((x, 0), (0, 0, 0))
            coord[x][0] = 1

        if coord[x][height-1] == -1:
            image1.putpixel((x, height-1), (0, 0, 0))
            coord[x][height-1] = 1

    for y in range(2, height-2):
        for x in range(2, width-2):
            if coord[x][y] == -1:
                BilinealInterpolationOnePixel(image1, coord, x, y)

    return image1

def BilinealInterpolationOnePixel(bmpOutput, coord, x, y):
    x0 = x
    x1 = x
    y0 = y
    y1 = y
    while coord[x0][y] == -1:
        x0 -= 1

    while coord[x1][y] == -1:
        x1 += 1

    while coord[x][y0] == -1:
        y0 -= 1

    while coord[x][y1] == -1:
        y1 += 1

    Hfactor = 1.0 * (x - x0) / (x1 - x0)
    Vfactor = 1.0 * (y - y0) / (y1 - y0)
    hr = bmpOutput.getpixel((x0, y))[0] + (bmpOutput.getpixel((x1, y))[0] - bmpOutput.getpixel((x0, y))[0]) * Hfactor
    hg = bmpOutput.getpixel((x0, y))[1] + (bmpOutput.getpixel((x1, y))[1] - bmpOutput.getpixel((x0, y))[1]) * Hfactor
    hb = bmpOutput.getpixel((x0, y))[2] + (bmpOutput.getpixel((x1, y))[2] - bmpOutput.getpixel((x0, y))[2]) * Hfactor
    vr = bmpOutput.getpixel((x, y0))[0] + (bmpOutput.getpixel((x, y1))[0] - bmpOutput.getpixel((x, y0))[0]) * Vfactor
    vg = bmpOutput.getpixel((x, y0))[1] + (bmpOutput.getpixel((x, y1))[1] - bmpOutput.getpixel((x, y0))[1]) * Vfactor
    vb = bmpOutput.getpixel((x, y0))[2] + (bmpOutput.getpixel((x, y1))[2] - bmpOutput.getpixel((x, y0))[2]) * Vfactor

    bmpOutput.putpixel((x,y),(int((hr + vr) / 2), int((hb + vb) / 2), int((hg + vg) / 2)))
    coord[x][y] = 1
