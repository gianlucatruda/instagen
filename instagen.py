#!/usr/bin/env python
# Image Generator for Instagram
# Version 1.7

version = "1.7"

import scipy.misc
import numpy as np
import random as rand
import datetime as dt
import math
import sys

# Image size as per Instagram 2017 = 1080x1080
full_scale = 1080
preview_scale = 300

# Generate session constants
foo = int(rand.randint(1, 80) * math.pi)
chunk = [3, 7, 9, 11][rand.randint(0, 3)]
# print(foo, chunk)

def get_norm(x, y):
    start = min(x, y)
    end = max(x, y)
    miu = int((end - start) / 2)
    dev = max(int((end - start) / 20), 1)
    return int(np.random.normal(miu, dev, 1)[0])


def get_values(x, y):
    bar = get_norm(x, y)
    r = get_norm(0, 200 - foo)
    g = get_norm(patternate(bar), r)
    b = get_norm(bar, patternate(g))
    return [r, g, b]


def patternate(x):
    return rand.randint(min(foo, x), max(foo, x))


def generate(width, height, type):
    # Create an empty image
    channels = 3
    img = np.zeros((height, width, channels), dtype=np.uint8)


    # Loop through every point in image
    current_cluster = get_values(0, 0)
    for x in range(width):
        for y in range(height):
            if (x % 20 == 0):
                print('\r' + str(round(100 * x / width)) + '%', end='...')
            if (y > 0 and x % y == chunk):
                current_cluster = get_values(patternate(x), y)
            img[y][x] = current_cluster


    # Save the image
    stamp = "{:%Y-%m-%d_%H-%M-%S}".format(dt.datetime.now())
    scipy.misc.imsave("output/" + type + "_v" + version + "_" + stamp + ".png", img)
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
