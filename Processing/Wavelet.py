import numpy as np
import pywt
import numpy
import PIL
from PIL import Image

def getWaveletCoefficients(imageArray, scales) :
    if scales == 0 :
        return imageArray
    CA, (CH,CV,CD) = pywt.dwt2(imageArray, 'haar')
    CA = getWaveletCoefficients(CA, scales-1)
    return join(CA, CH * 255, CV * 255, CD * 255)
    
def join(CA, CH, CV, CD):
    AH = np.hstack((CA, CH))
    VD = np.hstack((CV, CD))
    return np.vstack((AH, VD))

def getWavelet(fileName, scales):
    image = PIL.Image.open(fileName).convert("L")
    imageArray = numpy.array(image)
    wavelet = Image.fromarray(getWaveletCoefficients(imageArray, scales))
    return wavelet
    #wavelet.show()
