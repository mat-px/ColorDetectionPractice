######################################################################
#Programmer: Mateusz Przezdziecki date: 2/2/21
#File: green_screen.py
#Purpose: Key out an image on a green screen and paste it on another
#background.
######################################################################

import cv2
import numpy as np
import os
import matplotlib.image as mpimg  # mpimg.imread(path)
import matplotlib.pyplot as plt  # plt.imshow(np.array)

tiger = mpimg.imread('tiger.jpg')
swamp = mpimg.imread('swamp.jpg')

swamp = cv2.resize(swamp, dsize=(1280, 720), interpolation=cv2.INTER_CUBIC)

g0 = np.array([0, 150, 0])
g1 = np.array([120, 255, 120])

green_mask = cv2.inRange(tiger, g0, g1)
green_mask = np.dstack((green_mask, green_mask, green_mask))

tiger_background = np.copy(tiger)
tiger_background = np.where(green_mask==(0, 0, 0), tiger, swamp)

plt.imshow(tiger_background)
plt.show()
