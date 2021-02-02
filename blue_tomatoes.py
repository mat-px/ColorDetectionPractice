######################################################################
#Programmer: Mateusz Przezdziecki date: 1/30/21
#File: prac_proj_1.py
#Purpose: Change the color of a single color.
######################################################################

import numpy as np
import matplotlib.image as mpimg  # mpimg.imread(path)
import matplotlib.pyplot as plt  # plt.imshow(np.array)
from scipy.ndimage import generic_filter, convolve
import cv2  # cv2.kmeans and prebuilt computer vision functions ie grayscale

#Load image and make a copy
image = mpimg.imread('salad.jpg')


plt.imshow(output_image)
plt.show()
