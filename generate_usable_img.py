import random
import numpy as np

from skimage import color #For HSV
from scipy.misc import imsave #For HSV

#Create consistent image (perfect lines, HSV hue in [0, 1])
img = np.zeros((300,300,3), dtype='float32')

for i in range(img.shape[1]):
  img[:,i,:] = i / img.shape[1], 1.0, 1.0

#As perfect line
rgb_img = color.convert_colorspace(img, 'HSV', 'RGB')
imsave( 'testing_perfect.png', rgb_img )

#Shuffled
for i in range(img.shape[0]):
  np.random.shuffle( img[i,:,:] )

rgb_shuffled = color.convert_colorspace(img, 'HSV', 'RGB')
imsave( 'testing_shuffled.png', rgb_shuffled )
