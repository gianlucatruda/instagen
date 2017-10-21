import numpy as np
import random as rand


def get_norm(x, y):
    start = min(x, y)
    end = max(x, y)
    miu = int((end - start) / 2)
    dev = max(int((end - start) / 20), 1)
    return int(np.random.normal(miu, dev, 1)[0])


def get_values(x, y):
    bar = get_norm(x, y)
    r = get_norm(0, 200)
    g = get_norm(bar, r)
    b = get_norm(bar, g)
    return [r, g, b]
