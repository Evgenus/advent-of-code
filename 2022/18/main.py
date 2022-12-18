from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return {
        tuple(lmap(int, line.split(',')))
        for line in data.strip().splitlines()
    }


OFFSETS = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0),
]


def task1(filename):
    lava = read_data(filename)
    res = 0
    for x, y, z in lava:
        for dx, dy, dz in OFFSETS:
            if (x + dx, y + dy, z + dz) not in lava:
                res += 1
    return res


def bounds(items):
    return min(items) - 1, max(items) + 1


def task2(filename):
    lava = read_data(filename)

    minx, maxx = bounds([x for x, _, _ in lava])
    miny, maxy = bounds([y for _, y, _ in lava])
    minz, maxz = bounds([z for _, _, z in lava])

    water = set()
    queue = deque()
    queue.append((minx, miny, minz))
    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) in water:
            continue
        water.add((x, y, z))
        for dx, dy, dz in OFFSETS:
            nx, ny, nz = x + dx, y + dy, z + dz
            if not minx <= nx <= maxx:
                continue
            if not miny <= ny <= maxy:
                continue
            if not minz <= nz <= maxz:
                continue
            if (nx, ny, nz) not in lava:
                queue.append((nx, ny, nz))

    lava = {
        (x, y, z)
        for x in range(minx, maxx + 1)
        for y in range(miny, maxy + 1)
        for z in range(minz, maxz + 1)
        if (x, y, z) not in water
    }

    res = 0
    for x, y, z in lava:
        for dx, dy, dz in OFFSETS:
            if (x + dx, y + dy, z + dz) not in lava:
                res += 1
    return res


assert task1('test.txt') == 64
assert task1('data.txt') == 3364
assert task2('test.txt') == 58
assert task2('data.txt') == 2006
