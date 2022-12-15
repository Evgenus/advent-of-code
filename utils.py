from collections import deque
from functools import reduce
from itertools import (
    groupby,
)
import re
from typing import (
    Callable,
    Collection,
    Iterable,
    Iterator,
)


def load_input():
    import json
    import os.path
    home = os.path.dirname(os.path.join(__file__))
    session_path = os.path.join(home, 'session.json')
    with open(session_path, 'r') as stream:
        session_data = json.loads(stream.read())
    token = session_data['session']

    cwd = os.getcwd()
    cwd, day = os.path.split(cwd)
    day = day.lstrip('0')
    cwd, year = os.path.split(cwd)

    import urllib.request
    import urllib.error
    import shutil
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ("Cookie", "session={}".format(token)),
        ("User-Agent", "python-requests/2.19.1"),
    ]

    url = "https://adventofcode.com/{}/day/{}/input".format(year, day)
    with opener.open(url) as r:
        with open("data.txt", "wb") as f:
            shutil.copyfileobj(r, f)


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


def matrix_drawline(matrix, a, b, value):
    while a != b:
        i, j = a
        matrix[i][j] = value
        a = cell_move_towards(a, b)
    i, j = a
    matrix[i][j] = value


def matrix_print(matrix, translation=None):
    translation = translation or {}

    def stringify(cell) -> str:
        if cell in translation:
            return str(translation[cell])
        if isinstance(cell, float):
            return f'{cell:.2}'
        return str(cell)

    stringified = [
        [stringify(cell) for cell in row]
        for row in matrix
    ]

    max_len = max(
        len(cell)
        for row in stringified
        for cell in row
    )

    for row in stringified:
        for cell in row:
            print(f'{cell:>{max_len}}', end=' ')
        print()


def matrix_boundaries(matrix, func):
    top = len(matrix) - 1
    bottom = 0
    left = len(matrix[0]) - 1
    right = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if func(matrix[i][j]):
                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)

    return top, bottom, left, right


def matrix_crop(matrix, top, bottom, left, right):
    return [
        row[left: right + 1]
        for row in matrix[top: bottom + 1]
    ]


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


def str_group(s: str) -> list[str]:
    """
    >>> list(str_group("aaabbbccc"))
    ['aaa', 'bbb', 'ccc']
    """
    return [
        ''.join(group)
        for _, group in groupby(s)
    ]


def str_integers(s: str) -> list[int]:
    """
    >>> str_integers("12345")
    [12345]
    >>> str_integers("send 5 from 12345 to 67890")
    [5, 12345, 67890]
    >>> str_integers("send -5 from 12345 to 67890")
    [-5, 12345, 67890]
    """
    return lmap(int, re.findall(r'-{,1}\d+', s))


# LISTS


def iter_chunks(s: Collection, n: int) -> Iterator:
    """
    >>> list(iter_chunks("123456789", 3))
    ['123', '456', '789']
    >>> list(iter_chunks([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
    [[1, 2], [3, 4], [5, 6], [7, 8]]
    """
    for i in range(0, len(s) - n + 1, n):
        yield s[i: i + n]


def iter_window(s: Collection, n: int) -> Iterator:
    """
    >>> list(iter_window("123456789", 3))
    ['123', '234', '345', '456', '567', '678', '789']
    >>> list(iter_window([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
    [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]
    """
    for i in range(len(s) - n + 1):
        yield s[i: i + n]


def is_subsequence(s: Iterable, t: Iterable) -> bool:
    """
    >>> is_subsequence("abc", "ahbgdc")
    True
    >>> is_subsequence("axc", "ahbgdc")
    False
    """
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


def lmap(func: Callable, sequence: Iterable) -> list:
    """
    >>> lmap(int, "12345")
    [1, 2, 3, 4, 5]
    """
    return list(map(func, sequence))


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


# DICTIONARIES

def dict_swap(mapping: dict) -> dict:
    """
    >>> dict_swap({"a": 1, "b": 2, "c": 3})
    {1: 'a', 2: 'b', 3: 'c'}
    """
    return {v: k for k, v in mapping.items()}


def dict_invert(mapping: dict) -> dict:
    """
    >>> dict_invert({"a": 1, "b": 2, "c": 3})
    {1: ['a'], 2: ['b'], 3: ['c']}
    >>> dict_invert({"a": 1, "b": 2, "c": 1})
    {1: ['a', 'c'], 2: ['b']}
    """
    result = {}
    for k, v in mapping.items():
        result.setdefault(v, []).append(k)
    return result
