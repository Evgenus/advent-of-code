from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return {
        (i, j): int(char)
        for i, line in enumerate(data.strip().splitlines())
        for j, char in enumerate(line)
    }


def task1(filename):
    data = read_data(filename)

    return sum(
        v + 1
        for (i, j), v in data.items()
        if all(
            data.get((dx, dy), 9) > v
            for dx, dy in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j))
        )
    )


def task2(filename):
    data = read_data(filename)

    basins = []
    visited = set()
    for (i, j), v in data.items():
        if v == 9:
            continue
        queue = deque()
        queue.append((i, j))
        basin = 0
        while queue:
            i, j = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            basin += 1
            for dx, dy in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                if (dx, dy) in visited:
                    continue
                if (dx, dy) not in data:
                    continue
                if data[(dx, dy)] == 9:
                    continue
                queue.append((dx, dy))
        basins.append(basin)

    return mul(sorted(basins)[-3:])


assert task1('test.txt') == 15
assert task1('data.txt') == 560
assert task2('test.txt') == 1134
assert task2('data.txt') == 959136
