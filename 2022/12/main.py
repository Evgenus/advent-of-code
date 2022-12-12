from utils import (
    bfs,
    matrix_next4,
)


def read_data():
    with open('data.txt', 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()

    matrix = [list(line) for line in lines]

    start = None
    end = None

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == 'S':
                start = (row, col)
                cell = 'a'
            elif cell == 'E':
                end = (row, col)
                cell = 'z'

            matrix[row][col] = ord(cell) - ord('a')

    matrix: list[list[int]]
    return matrix, start, end


def task1():
    matrix, start, end = read_data()
    for (row, col), queue, step in bfs(start):
        if (row, col) == end:
            return step
        cell = matrix[row][col]
        for r, c in matrix_next4(matrix, row, col):
            next_cell = matrix[r][c]
            if next_cell <= cell + 1:
                queue.append((r, c))

    return -1


def task2():
    matrix, start, end = read_data()
    for (row, col), queue, step in bfs(end):
        cell = matrix[row][col]
        if cell == 0:
            return step
        for r, c in matrix_next4(matrix, row, col):
            next_cell = matrix[r][c]
            if cell <= next_cell + 1:
                queue.append((r, c))

    return -1


print(task1())
print(task2())
