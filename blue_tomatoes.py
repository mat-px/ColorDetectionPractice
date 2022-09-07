######################################################################
#Programmer: Mateusz Przezdziecki date: 1/30/21
#File: blue_tomatoes.py
#Purpose: Detect a range of colors and change the color of them.
######################################################################

import numpy as np
import matplotlib.image as mpimg  # mpimg.imread(path)
import matplotlib.pyplot as plt  # plt.imshow(np.array)
from scipy.ndimage import generic_filter, convolve
import cv2  # cv2.kmeans and prebuilt computer vision functions ie grayscale

# Load image and make a copy
salad = mpimg.imread('salad.jpg')

vectorized = salad.reshape((-1, 3))
vectorized = np.float32(vectorized)

# Constants for cv2.kmeans
termination_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K = 9
_, label, center = cv2.kmeans(vectorized, K, bestLabels=None, criteria=termination_criteria, attempts=10, flags=0)

# Color code pixels based on their class and the centroid color of their class
result_image = np.uint8(center)[label.flatten()]
result_image = result_image.reshape((salad.shape))

# Red Boundaries
red0 = np.array([150, 0, 0])
red1 = np.array([250, 130, 80])

mask = cv2.inRange(result_image, red0, red1)
mask = np.dstack((mask, mask, mask))

blue_tomato = np.copy(salad)

# np.where(NOT RED, KEEP THE SAME COLOR, IF RED CHANGE TO THIS)
blue_tomato = np.where(mask==(0, 0, 0), blue_tomato, 255 - blue_tomato)

#Saves Image
plt.imsave("blue_tomatoes.jpg", blue_tomato)

plt.imshow(blue_tomato)
plt.show()
