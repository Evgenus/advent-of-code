def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return [
        list(line[1: -1])
        for line in data.strip().splitlines()[1:-1]
    ]


directions = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0),
}


class Solver:
    def __init__(self, board):
        self.board = board
        self.n = len(board)
        self.m = len(board[0])

        self.blizzards = [
            ((i, j), directions[char])
            for i, line in enumerate(board)
            for j, char in enumerate(line)
            if char in directions
        ]

    def travel(self, step, start, end):
        step += 1
        queue = set()
        while True:
            step += 1
            forbidden = {
                ((i + di * step) % self.n, (j + dj * step) % self.m)
                for (i, j), (di, dj) in self.blizzards
            }

            queue.add(start)
            next_queue = set()
            for i, j in queue:
                if (i, j) == end:
                    return step
                for ni, nj in (i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if not 0 <= ni < self.n:
                        continue
                    if not 0 <= nj < self.m:
                        continue
                    if (ni, nj) in forbidden:
                        continue
                    next_queue.add((ni, nj))
            queue = next_queue


def task1(filename):
    board = read_data(filename)

    solver = Solver(board)
    start = (0, 0)
    end = (solver.n - 1, solver.m - 1)
    return solver.travel(0, start, end)


def task2(filename):
    board = read_data(filename)

    solver = Solver(board)
    start = (0, 0)
    end = (solver.n - 1, solver.m - 1)
    t1 = solver.travel(0, start, end)
    t2 = solver.travel(t1, end, start)
    t3 = solver.travel(t2, start, end)
    return t3


assert task1('test.txt') == 18
assert task1('data.txt') == 242
assert task2('test.txt') == 54
assert task2('data.txt') == 720
