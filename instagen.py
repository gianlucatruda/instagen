#!/usr/bin/env python
# Image Generator for Instagram
version = "2.1"

import math, sys, scipy.misc
import random as rand
from functions import *
import datetime as dt


# Image size as per Instagram 2017 = 1080x1080
full_scale = 1080
preview_scale = 300

# Session constants
foo = int(rand.randint(1, 80) * math.pi)
chunk = rand.randint(1, foo)
pallet = get_pallet(foo)


def generate(width, height, kind):
    # Create an empty image
    channels = 3
    img = np.zeros((height, width, channels), dtype=np.uint8)

    # Loop through every point in image
    current_cluster = get_pixel(0, 0, pallet)
    for x in range(width):
        for y in range(height):
            if x % 20 == 0:
                print('\r' + str(round(100 * x / width)) + '%', end='...')
            if y > 0 and x > 0 and (x % chunk == 0 or y % chunk == 0):
                current_cluster = get_pixel(x, y, pallet)
            img[y][x] = current_cluster

    # Save the image
    stamp = "{:%Y-%m-%d_%H-%M-%S}".format(dt.datetime.now())
    scipy.misc.imsave("output/" + kind + "_v" + version + "_" + stamp + ".png", img)
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
