import numpy as np
from PIL import Image

import random

#Interchangeable with np.random.randint
#newImage = np.zeros((300,300,3), dtype='uint8')
#
#for x in range(newImage.shape[0]):
#  for y in range(newImage.shape[1]):
#    newImage[x,y] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

#Interchangeable with np.zeroes + range().  This is faster
newImage = np.random.randint(0, 255, (300,300,3))

#Uses RGB, which is a 3D cube.  Moving to HSV, which is cylindrical, (hue is circle, saturation is radius, value is height), can sort linearly as hue

#Random Image
testImage = Image.fromarray(newImage.astype('uint8'))
testImage.save('test_random.png')
