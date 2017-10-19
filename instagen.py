#!/usr/bin/env python
# Image Generator for Instagram
# Version 1.4

version = "1.4"

import scipy.misc
import numpy as np
import random as rand
import datetime as dt
import math
import sys

# Image size as per Instagram 2017 = 1080x1080
full_scale = 1080
preview_scale = 300

def get_norm(x, y):
	start = min(x,y)
	end = max(x,y)
	miu = int((end-start)/2)
	dev = max(int((end-start)/20),1)
	return int(np.random.normal(miu, dev, 1)[0])

def get_values(x,y):
	a = get_norm(0, 200)
	b = get_norm(200, 255)
	c = int((a/(b+1))*256)
	return [a, b, c]

def generate(width, height, type):
	# Create an empty image
	channels = 3
	img = np.zeros((height, width, channels), dtype=np.uint8)

	for x in range(width):
		for y in range(height):
			if(x%100==0):
				print('\r'+str(round(100*x/width))+'%',end='...')
			img[y][x] = get_values(x,y)

	# Save the image
	stamp = "{:%Y-%m-%d_%H-%M-%S}".format(dt.datetime.now())
	scipy.misc.imsave("output/"+type+"_v"+version+"_"+stamp+".png", img)
	print("\r100%...Image saved")

def gen_preview():
	generate(preview_scale, preview_scale, "prev")

def gen_full():
	generate(full_scale, full_scale, "gen")

if __name__ == "__main__":
	argv = sys.argv[1:]
	if len(argv) >= 1:
		gen_full()
	else:
		gen_preview()
