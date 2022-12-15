from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    sensors = {}
    beacons = set()
    for line in lines:
        sx, sy, bx, by = str_integers(line)
        dist = cell_dist4((sx, sy), (bx, by))
        sensors[sx, sy] = dist
        beacons.add((bx, by))

    return sensors, beacons


def check(distances, x, y):
    for sx, sy in distances:
        if cell_dist4((sx, sy), (x, y)) <= distances[sx, sy]:
            return False
    return True


def task1(filename, row):
    sensors, beacons = read_data(filename)

    minx = float('inf')
    maxx = -float('inf')

    for a, d in sensors.items():
        r = (d - abs(a[1] - row))
        minx = min(minx, a[0] - r)
        maxx = max(maxx, a[0] + r)

    beacons = {x for x, y in beacons if y == row}
    res = 0
    for x in range(minx, maxx + 1):
        if x in beacons:
            continue
        res += not check(sensors, x, row)
    return res


def task2(filename, cap):
    sensors, _ = read_data(filename)

    for a, d in sensors.items():
        d += 1
        for y in range(a[1] - d, a[1] + d):
            if y > cap or y < 0:
                break
            r = (d - abs(a[1] - y))
            x1 = a[0] - r
            x2 = a[0] + r
            if 0 <= x1 <= cap and check(sensors, x1, y):
                return x1 * 4000000 + y
            if 0 <= x2 <= cap and check(sensors, x2, y):
                return x2 * 4000000 + y


assert task1('test.txt', 10) == 26
assert task1('data.txt', 2000000) == 4793062
assert task2('test.txt', 20) == 56000011
assert task2('data.txt', 4000000) == 10826395253551
