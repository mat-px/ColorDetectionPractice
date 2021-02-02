######################################################################
#Programmer: Mateusz Przezdziecki date: 1/28/21
#File: prac_proj_1.py
#Purpose: Change the color scheme of Mario.
######################################################################

import numpy as np
import matplotlib.image as mpimg  # mpimg.imread(path)
import matplotlib.pyplot as plt  # plt.imshow(np.array)

#Load image and make a copy
mario = mpimg.imread('8BitMario.jpg')
wario = np.copy(mario)

#Background
white_spots = np.mean(wario, axis=2) >= 254
wario[white_spots] = np.array([30, 30, 30])

#Shoulders
green_spots = np.sum(wario[350:650,:,:], axis=2) == 255
wario[350:650,:,:][green_spots] = np.array([255, 255, 0])

#Hair
green_spots = np.sum(wario[0:350,:,:], axis=2) == 255
wario[0:350,:,:][green_spots] = np.array([0, 0, 0])

#Hat
red_spots = np.sum(wario[0:350,:,:], axis=2) == 361
wario[0:350,:,:][red_spots] = np.array([255, 255, 0])

#Overalls
red_spots = np.sum(wario[350:,:,:], axis=2) == 361
wario[350:,:,:][red_spots] = np.array([255, 0, 255])

#Button and Hand
orange_spots = np.sum(wario[450:,:,:], axis=2) == 406
wario[450:,:,:][orange_spots] = np.array([255, 255, 255])

#Stretches the image
wario_h, wario_w, _ = wario.shape
wario = wario[np.arange(0, wario_h, 2)]

#Print Image
plt.imshow(wario)
plt.show()
