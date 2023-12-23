import sys


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


slopes = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0),
}


sys.setrecursionlimit(100000)


def task1(filename):
    lines = read_data(filename)
    matrix = list(map(list, lines))

    n = len(matrix)
    m = len(matrix[0])

    start, = [j for j, c in enumerate(matrix[0]) if c != '#']
    end, = [j for j, c in enumerate(matrix[-1]) if c != '#']
    result = []
    path = []

    def dfs(i, j):
        if (i, j) == (n - 1, end):
            result.append(list(path))
        path.append((i, j))
        matrix[i][j] = 'O'

        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if not 0 <= ni < n:
                continue
            if not 0 <= nj < m:
                continue
            if matrix[ni][nj] == '.':
                dfs(ni, nj)
            elif matrix[ni][nj] in slopes:
                slope = matrix[ni][nj]
                if slopes[slope] == (di, dj):
                    path.append((ni, nj))
                    matrix[ni][nj] = 'O'
                    dfs(ni + di, nj + dj)
                    matrix[ni][nj] = slope
                    path.pop()
        matrix[i][j] = '.'
        path.pop()

    dfs(0, start)
    return max(map(len, result))


assert task1('test.txt') == 94
assert task1('data.txt') == 2130
