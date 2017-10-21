import numpy as np
import random as rand


def rand_chanel():
    return rand.randint(0, 256)


def rand_colour():
    return [rand_chanel(), rand_chanel(), rand_chanel()]


def supplementary_colour(colour):
    r = 256 - colour[0]
    g = 256 - colour[1]
    b = 256 - colour[2]
    return [r, g, b]


def get_norm(x, y):
    start = min(x, y)
    end = max(x, y)
    miu = int((end - start) / 2)
    dev = max(int((end - start) / 20), 1)
    return int(np.random.normal(miu, dev, 1)[0])


def get_pallet(cons):
    primary = rand_colour()
    secondary = supplementary_colour(primary)
    return [primary, secondary]


def get_pixel(x, y, pallet):
    c1 = pallet[x % 2]
    c2 = pallet[y % 2]
    r = get_norm(c1[0], c2[0])
    g = get_norm(c2[1], c1[1])
    b = get_norm(c1[2], c2[2])
    return [r, g, b]

