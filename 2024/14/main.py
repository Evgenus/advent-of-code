from utils import *
from collections import Counter
from itertools import pairwise
from PIL import Image


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename, w, h):
    lines = read_data(filename)
    lines = lmap(str_integers, lines)
    result = 0

    q1, q2, q3, q4 = 0, 0, 0, 0
    t = 100
    for px, py, vx, vy in lines:
        px = (px + vx * t) % w
        py = (py + vy * t) % h

        if px > w // 2:
            if py > h // 2:
                q1 += 1
            elif py < h // 2:
                q2 += 1
        elif px < w // 2:
            if py > h // 2:
                q3 += 1
            elif py < h // 2:
                q4 += 1

    result = q1 * q2 * q3 * q4

    print(f"1: {filename}, {result}")
    return result


def task2(filename, w, h):
    lines = read_data(filename)
    lines = lmap(str_integers, lines)
    result = 0

    p = 101
    for i in range(100):
        t = 70 + i * 101
        img = Image.new('RGB', (w, h))

        for px, py, vx, vy in lines:
            px = (px + vx * t) % w
            py = (py + vy * t) % h
            img.putpixel((px, py), (255, 255, 255))
        img.save(f'{t}.png')

    print(f"2: {filename}, {result}")
    return result


load_input()
assert task1('test.txt', 11, 7) == 12
assert task1('data.txt', 101, 103) == 225648864
# task2('data.txt', 101, 103)
