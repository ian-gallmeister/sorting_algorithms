import random
import numpy as np

from skimage import color #For HSV
from scipy.misc import imsave #For HSV

newImage = np.random.randint(0, 255, (300,300,3))

#Uses RGB, which is a 3D cube.  Moving to HSV, which is cylindrical, (hue is circle, saturation is radius, value is height), can sort linearly as hue

#Basic Sorts
hsv_hue = color.convert_colorspace(newImage, 'RGB', 'HSV')
hsv_sat = hsv_hue.copy()
hsv_val = hsv_hue.copy()

#By hue, saturation, and value
for i in range(newImage.shape[0]):
  hsv_hue[i,:,0] = np.sort(hsv_hue[i,:,0])
  hsv_sat[i,:,1] = np.sort(hsv_sat[i,:,1])
  hsv_val[i,:,2] = np.sort(hsv_val[i,:,2])

imsave('test_hue_sort.png',color.convert_colorspace(hsv_hue, 'HSV', 'RGB'))
imsave('test_sat_sort.png',color.convert_colorspace(hsv_sat, 'HSV', 'RGB'))
imsave('test_val_sort.png',color.convert_colorspace(hsv_val, 'HSV', 'RGB'))
