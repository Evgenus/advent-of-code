from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    maze, (path, ) = list_split(data.splitlines(), [''])

    n = len(maze)
    m = max(len(row) for row in maze)
    matrix = [
        [' '] * m for _ in range(n)
    ]
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            matrix[i][j] = char

    path = path.replace('L', ' L ').replace('R', ' R ').split()
    return matrix, path


R = 0
D = 1
L = 2
U = 3


DIRECTIONS = {
    R: (0, 1),
    D: (1, 0),
    L: (0, -1),
    U: (-1, 0),
}


class Solution:
    def __init__(self, matrix, cube_layout, transitions):
        self.matrix = matrix
        self.cube_layout = cube_layout
        self.transitions = transitions
        n = len(matrix)
        m = len(matrix[0])
        self.cube_size = max(n, m) // 4

    def jump(self, ci, cj, d1, d2):
        """
        jump from one side of the cube to the other
        ci, cj - coordinates on side of cube
        d1 - previous direction
        d2 - new direction
        """
        s = self.cube_size - 1
        axis_changed = abs(DIRECTIONS[d1][0]) != abs(DIRECTIONS[d2][0])
        sign_changed = sum(DIRECTIONS[d1]) * sum(DIRECTIONS[d2]) < 0

        if axis_changed:
            ci, cj = cj, ci  # swap coordinates
            sign_changed = not sign_changed  # swap sign

        if sign_changed:
            ci, cj = s - ci, s - cj  # flip coordinates

        return [(ci, 0), (0, cj), (ci, s), (s, cj)][d2]

    def get_side_number(self, mi, mj) -> int:
        size = self.cube_size
        cube_coords = mi // size, mj // size
        for cube_num, coords in self.cube_layout.items():
            if coords == cube_coords:
                return cube_num
        assert 0

    def get_coord_on_side(self, mi, mj):
        size = self.cube_size
        return mi % size, mj % size

    def get_matrix_coords(self, ci, cj, side_num):
        size = self.cube_size
        side_i, side_j = self.cube_layout[side_num]
        return side_i * size + ci, side_j * size + cj

    def move(self, mi, mj, d):
        di, dj = DIRECTIONS[d]

        side = self.get_side_number(mi, mj)
        ci, cj = self.get_coord_on_side(mi, mj)

        if not 0 <= ci + di < self.cube_size or not 0 <= cj + dj < self.cube_size:
            side, new_d = self.transitions[side, d]
            ci, cj = self.jump(ci, cj, d, new_d)
            mi, mj = self.get_matrix_coords(ci, cj, side)
            return mi, mj, new_d
        else:
            return mi + di, mj + dj, d

    def solve(self, path, i, j, d):
        for command in path:
            if command == 'L':
                d = (d - 1) % 4
            elif command == 'R':
                d = (d + 1) % 4
            else:
                dist = int(command)
                for _ in range(dist):
                    ni, nj, nd = self.move(i, j, d)  # try to move
                    if self.matrix[ni][nj] == '.':  # can move
                        i, j, d = ni, nj, nd
                    elif self.matrix[ni][nj] == '#':  # can't move
                        break
        return i, j, d


def task(data, layout, transitions):
    matrix, path = read_data(data)

    solver = Solution(matrix, layout, transitions)
    i, j, d = solver.solve(path, 0, matrix[0].index('.'), R)

    return 1000 * (i + 1) + 4 * (j + 1) + d


CUBE_LAYOUT_TEST = {
    1: (0, 2),
    2: (1, 0),
    3: (1, 1),
    4: (1, 2),
    5: (2, 2),
    6: (2, 3),
}

CUBE_LAYOUT_DATA = {
    1: (0, 1),
    2: (0, 2),
    3: (1, 1),
    4: (2, 1),
    5: (2, 0),
    6: (3, 0),
}


TRANSITIONS_TEST_1 = {
    (1, R): (1, R),
    (1, D): (4, D),
    (1, L): (1, L),
    (1, U): (5, U),

    (2, R): (3, R),
    (2, D): (2, D),
    (2, L): (4, L),
    (2, U): (2, U),

    (3, R): (4, R),
    (3, D): (3, D),
    (3, L): (2, L),
    (3, U): (3, U),

    (4, R): (2, R),
    (4, D): (5, D),
    (4, L): (3, L),
    (4, U): (1, U),

    (5, R): (6, R),
    (5, D): (1, D),
    (5, L): (6, L),
    (5, U): (4, U),

    (6, R): (5, R),
    (6, D): (6, D),
    (6, L): (5, L),
    (6, U): (6, U),
}


TRANSITIONS_DATA_1 = {
    (1, L): (2, L),
    (1, D): (3, D),
    (1, R): (2, R),
    (1, U): (4, U),

    (2, L): (1, L),
    (2, D): (2, D),
    (2, R): (1, R),
    (2, U): (2, U),

    (3, R): (3, R),
    (3, D): (4, D),
    (3, L): (3, L),
    (3, U): (1, U),

    (4, R): (5, R),
    (4, D): (1, D),
    (4, L): (5, L),
    (4, U): (3, U),

    (5, R): (4, R),
    (5, D): (6, D),
    (5, L): (4, L),
    (5, U): (6, U),

    (6, R): (6, R),
    (6, D): (5, D),
    (6, L): (6, L),
    (6, U): (5, U),
}


TRANSITIONS_TEST_2 = {
    (1, R): (6, L),
    (1, D): (4, D),
    (1, L): (3, D),
    (1, U): (2, D),

    (2, R): (3, R),
    (2, D): (5, U),
    (2, L): (6, U),
    (2, U): (1, D),

    (3, R): (4, R),
    (3, D): (5, R),
    (3, L): (2, L),
    (3, U): (1, R),

    (4, R): (6, D),
    (4, D): (5, D),
    (4, L): (3, L),
    (4, U): (1, U),

    (5, R): (6, R),
    (5, D): (2, U),
    (5, L): (3, U),
    (5, U): (4, U),

    (6, R): (1, L),
    (6, D): (2, R),
    (6, L): (5, L),
    (6, U): (4, L),
}


TRANSITIONS_DATA_2 = {
    (1, L): (5, R),
    (1, D): (3, D),
    (1, R): (2, R),
    (1, U): (6, R),

    (2, L): (1, L),
    (2, D): (3, L),
    (2, R): (4, L),
    (2, U): (6, U),

    (3, R): (2, U),
    (3, D): (4, D),
    (3, L): (5, D),
    (3, U): (1, U),

    (4, R): (2, L),
    (4, D): (6, L),
    (4, L): (5, L),
    (4, U): (3, U),

    (5, R): (4, R),
    (5, D): (6, D),
    (5, L): (1, R),
    (5, U): (3, R),

    (6, R): (4, U),
    (6, D): (2, D),
    (6, U): (5, U),
    (6, L): (1, D),
}


assert task('test.txt', CUBE_LAYOUT_TEST, TRANSITIONS_TEST_1) == 6032
assert task('data.txt', CUBE_LAYOUT_DATA, TRANSITIONS_DATA_1) == 190066
assert task('test.txt', CUBE_LAYOUT_TEST, TRANSITIONS_TEST_2) == 5031
assert task('data.txt', CUBE_LAYOUT_DATA, TRANSITIONS_DATA_2) == 134170
