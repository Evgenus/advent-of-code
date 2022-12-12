from collections import deque


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

    return matrix, start, end


def task1():
    matrix, start, end = read_data()
    visited = set()
    queue = deque()
    queue.append(start)
    step = 0
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if (row, col) == end:
                return step
            for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if not 0 <= r < len(matrix):
                    continue
                if not 0 <= c < len(matrix[row]):
                    continue
                if matrix[r][c] <= matrix[row][col] + 1:
                    queue.append((r, c))

        step += 1


def task2():
    matrix, start, end = read_data()
    visited = set()
    queue = deque()
    queue.append(end)
    step = 0
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if matrix[row][col] == 0:
                return step
            for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if not 0 <= r < len(matrix):
                    continue
                if not 0 <= c < len(matrix[row]):
                    continue
                if matrix[row][col] <= matrix[r][c] + 1:
                    queue.append((r, c))

        step += 1


print(task1())
print(task2())
