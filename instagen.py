#!/usr/bin/env python
# Image Generator for Instagram
# Version 1.3

version = "1.3"

import scipy.misc
import numpy as np
import random as rand
import datetime as dt
import math

# Image size as per Instagram 2017
width = 1080
height = 1080
channels = 3

def getPoint(min, max):
	miu = int((max-min)/2)
	dev = int((max-min)/20)
	return int(np.random.normal(miu, dev, 5)[0])

# Create an empty image
img = np.zeros((height, width, channels), dtype=np.uint8)


for i in range(width*height):
	if(i%width==0):
		print('\r'+str(round(100*i/(width*height)))+'%',end='...')
	a = int(math.sqrt(i))
	b = getPoint(100, 200)
	c = int((b/(a+1))*256)
	img[getPoint(0, height)][a] = [100, b, c]

# Save the image
stamp = "{:%Y-%m-%d_%H-%M-%S}".format(dt.datetime.now())
scipy.misc.imsave("output/gen_v"+version+"_"+stamp+".png", img)
print("Image saved")
