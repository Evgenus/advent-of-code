from collections import deque
from functools import reduce
from itertools import groupby
from typing import (
    Iterable,
    Iterator,
)


def chain(*funcs):
    """
    f = chain(f1, f2, f3, f4)

    is equivalent to

    f = lambda arg: f4(f3(f2(f1(arg))))
    """
    def chained(arg):
        return reduce(lambda r, f: f(r), funcs, arg)
    return chained


def matrix_next4(matrix, row, col):
    for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
        if not 0 <= r < len(matrix):
            continue
        if not 0 <= c < len(matrix[row]):
            continue
        yield r, c


def bfs(*start):
    visited = set()
    queue = deque()
    queue.extend(start)
    step = 0
    while queue:
        for _ in range(len(queue)):
            item = queue.popleft()
            if item in visited:
                continue
            visited.add(item)
            yield item, queue, step
        step += 1


# NUMBERS


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


# STRINGS


def str_common(*strings: str) -> str:
    """
    >>> str_common("abc", "abd", "cbe")
    'b'
    """
    return "".join(
        reduce(
            lambda x, y: x & y,
            map(set, strings),
        )
    )


def str_iter_chunks(s: str, n: int) -> Iterator[str]:
    """
    >>> list(str_iter_chunks("123456789", 3))
    ['123', '234', '345', '456', '567', '678', '789']
    """
    for i in range(len(s) - n + 1):
        yield s[i: i + n]


def str_group(s: str) -> list[str]:
    """
    >>> list(str_group("aaabbbccc"))
    ['aaa', 'bbb', 'ccc']
    """
    return [
        ''.join(group)
        for _, group in groupby(s)
    ]


# LISTS


def is_subsequence(self, s: Iterable, t: Iterable) -> bool:
    it = iter(t)
    return all(c in it for c in s)


def list_startswith(items: list, prefix: list) -> bool:
    """
    >>> list_startswith([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3])
    True
    >>> list_startswith([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4])
    False
    """
    return items[:len(prefix)] == prefix


def list_split(items: list, sep: list) -> list[list]:
    """
    >>> list_split([1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6])
    [[1, 2, 3], [7, 8, 9]]
    """
    result = []
    current = []
    i = 0
    while i < len(items):
        if list_startswith(items[i:], sep):
            result.append(current)
            current = []
            i += len(sep)
        else:
            current.append(items[i])
            i += 1
    if current:
        result.append(current)
    return result


# CELLS


def cell_dist4(a, b) -> int:
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    return dx + dy


def cell_dist8(a, b) -> int:
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    return max(dx, dy)


def cell_move_towards(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    return a[0] + sign(dx), a[1] + sign(dy)


# VECTORS

def triangle_area(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    m = s * (s - a) * (s - b) * (s - c)
    return abs(m) ** 0.5


def vect_length(p1, p2) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
