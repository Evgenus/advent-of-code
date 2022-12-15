from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    return lines


def task1(filename, row):
    lines = read_data(filename)
    distances = {}
    minx = float('inf')
    maxx = -float('inf')
    beacons = set()
    for line in lines:
        sx, sy, bx, by = str_integers(line)
        dist = cell_dist4((sx, sy), (bx, by))
        distances[sx, sy] = dist
        minx = min(minx, bx)
        maxx = max(maxx, bx)
        beacons.add((bx, by))

    beacons = {x for x, y in beacons if y == row}
    ranges = set()
    for sx, sy in distances:
        r = (distances[sx, sy] - abs(sy - row))
        if r >= 0:
            s = set(range(sx - r, sx + r + 1))
            ranges |= s

    ranges = ranges - beacons

    return len(ranges)
    # for col in range(10):


#load_input()
# print(task1('test.txt', 10))
# print(task1('data.txt', 2000000))


def task2(filename, cap):
    lines = read_data(filename)
    distances = {}
    minx = float('inf')
    maxx = -float('inf')
    beacons = set()
    for line in lines:
        sx, sy, bx, by = str_integers(line)
        dist = cell_dist4((sx, sy), (bx, by))
        distances[sx, sy] = dist
        minx = min(minx, bx)
        maxx = max(maxx, bx)
        beacons.add((bx, by))

    def check(x, y):
        for sx, sy in distances:
            if cell_dist4((sx, sy), (x, y)) <= distances[sx, sy]:
                return False
        return True

    sensors = list(distances.keys())
    for a in sensors:
        print('.')
        d = distances[a] + 1
        for y in range(a[1] - d, a[1] + d):
            if y > cap or y < 0:
                break
            r = (d - abs(a[1] - y))
            x1 = a[0] - r
            x2 = a[0] + r
            if 0 <= x1 <= cap and check(x1, y):
                return x1 * 4000000 + y
            if 0 <= x2 <= cap and check(x2, y):
                return x2 * 4000000 + y


#print(task2('test.txt'))
print(task2('data.txt', 4000000))
