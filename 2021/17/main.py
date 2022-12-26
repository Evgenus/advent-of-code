from collections import defaultdict

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    minx, maxx, miny, maxy = str_integers(data.strip())
    return minx, maxx, miny, maxy


def task1(filename):
    minx, maxx, miny, maxy = read_data(filename)
    return (miny + 1) * miny // 2


def task2(filename):
    minx, maxx, miny, maxy = read_data(filename)

    res = 0
    n = int((minx * 2) ** 0.5 - 1)

    dxs = defaultdict(set)
    for dx_init in range(n, maxx + 1):
        x, dx, step = 0, dx_init, 0
        while x <= maxx and (dx == 0 and minx <= x or dx != 0):
            x += dx
            if dx > 0:
                dx -= 1
            step += 1
            if minx <= x <= maxx:
                dxs[dx_init].add(step)
                if dx == 0:
                    dxs[dx_init] = min(dxs[dx_init])
                    break

    dys = defaultdict(set)
    for dy_init in range(miny, -miny):
        y, dy, step = 0, dy_init, 0
        while miny <= y:
            y += dy
            dy -= 1
            step += 1
            if miny <= y <= maxy:
                dys[dy_init].add(step)

    for xsteps in dxs.values():
        for ysteps in dys.values():
            if type(xsteps) is int:
                if xsteps <= max(ysteps):
                    res += 1
            elif xsteps & ysteps:
                res += 1

    return res


print(task1('test.txt'))
print(task1('data.txt'))
print(task2('test.txt'))
print(task2('data.txt'))
