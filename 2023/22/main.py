from collections import defaultdict

from utils import *
# load_input()


def get_cells(a, b):
    dx, dy, dz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
    while a != b:
        yield a
        a = a[0] + sign(dx), a[1] + sign(dy), a[2] + sign(dz)
    yield b


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()

    bricks = []
    for line in lines:
        _start, _end = line.split('~')
        start = tmap(int, _start.split(','))
        end = tmap(int, _end.split(','))
        bricks.append(list(get_cells(start, end)))

    return bricks


def make_fall(bricks):
    space = defaultdict(int)
    for index, brick in enumerate(bricks, start=1):
        for x, y, z in brick:
            space[x, y, z] = index

    while True:
        fall = False

        for index, brick in enumerate(bricks, start=1):
            if all(space[x, y, z - 1] in (0, index) and z > 0 for x, y, z in brick):
                fall = True
                for x, y, z in brick:
                    space[x, y, z] = 0
                for i, (x, y, z) in enumerate(brick):
                    brick[i] = x, y, z - 1
                for x, y, z in brick:
                    space[x, y, z] = index
        if not fall:
            break

    return space


def calculate_supports(bricks, space):
    supported = defaultdict(set)
    supports = defaultdict(set)
    for index, brick in enumerate(bricks, start=1):
        supports[index] = set()
        for x, y, z in brick:
            other = space[x, y, z + 1]
            if other not in (0, index):
                supported[other].add(index)
                supports[index].add(other)
    return supported, supports


def task1(filename):
    bricks = read_data(filename)
    space = make_fall(bricks)
    supported, supports = calculate_supports(bricks, space)

    result = 0
    for index, tops in supports.items():
        if all(supported[top] - {index} for top in tops):
            result += 1
    return result


def task2(filename):
    bricks = read_data(filename)
    space = make_fall(bricks)
    supported, supports = calculate_supports(bricks, space)

    result = 0
    for index, _ in enumerate(bricks, start=1):
        disintegrated = set()
        queue = deque()
        queue.append(index)
        while queue:
            block = queue.popleft()
            if block in disintegrated:
                continue
            disintegrated.add(block)

            for top in supports[block]:
                if top in disintegrated:
                    continue
                if supported[top] and not supported[top] - disintegrated:
                    queue.append(top)
        result += len(disintegrated - {index})

    return result


assert task1('test.txt') == 5
assert task1('data.txt') == 395
assert task2('test.txt') == 7
assert task2('data.txt') == 64714
