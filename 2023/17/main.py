import heapq

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    return [lmap(int, line) for line in lines]


directions = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

rev = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E",
    "?": "?",
}


def solve(matrix, min_dist, max_dist):
    n = len(matrix)
    m = len(matrix[0])
    queue = [(0, 0, 0, "?")]
    visited = set()
    loss = {}
    while queue:
        l, i, j, d = heapq.heappop(queue)
        if (i, j, d) in visited:
            continue
        if i == n - 1 and j == m - 1:
            return l
        visited.add((i, j, d))
        for nd, (di, dj) in directions.items():
            if nd == d or nd == rev[d]:
                continue
            dl = 0
            ni, nj = i, j
            for k in range(1, max_dist + 1):
                ni, nj = ni + di, nj + dj
                if not 0 <= ni < n:
                    break
                if not 0 <= nj < m:
                    break
                dl += matrix[ni][nj]
                if k < min_dist:
                    continue
                nl = l + dl
                if loss.get((ni, nj, nd), inf) <= nl:
                    continue
                loss[(ni, nj, nd)] = nl
                heapq.heappush(queue, (nl, ni, nj, nd))


def task1(filename):
    matrix = read_data(filename)
    return solve(matrix, 1, 3)


def task2(filename):
    matrix = read_data(filename)
    return solve(matrix, 4, 10)


assert task1('test.txt') == 102
assert task1('data.txt') == 907
assert task2('test.txt') == 94
assert task2('data.txt') == 1057
