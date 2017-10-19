#!/usr/bin/env python
# Image Generator for Instagram
# Version 1.1

version = "1.1"

import scipy.misc
import numpy as np
import random as rand
import datetime as dt

# Image size as per Instagram 2017
width = 1080
height = 1080
channels = 3

# Create an empty image
img = np.zeros((height, width, channels), dtype=np.uint8)

"""
# Draw something (http://stackoverflow.com/a/10032271/562769)
xx, yy = np.mgrid[:height, :width]
circle = (xx - 100) ** 2 + (yy - 100) ** 2

# Set the RGB values
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        r, g, b = circle[y][x], circle[y][x], circle[y][x]
        img[y][x][0] = r
        img[y][x][1] = g
        img[y][x][2] = b
"""

def getPoint():
	return np.random.normal(128, 50, 1)[0]

for y in range(img.shape[0]):
	for x in range(img.shape[1]):
		img[y][x][0] = rand.randint(100, 150)
		img[y][x][1] = rand.randint(100, 150)
		img[y][x][2] = rand.randint(100, 150)

# Save the image
stamp = "{:%Y-%m-%d_%H-%M-%S}".format(dt.datetime.now())
scipy.misc.imsave("gen_v"+version+"_"+stamp+".png", img)
