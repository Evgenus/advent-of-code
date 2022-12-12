from functools import reduce


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def dist4(a, b):
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    return dx + dy


def dist8(a, b):
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    return max(dx, dy)


def move_towards(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    return a[0] + sign(dx), a[1] + sign(dy)


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
    for i in range(len(items)):
        if items[i:i + len(sep)] == sep:
            result.append(current)
            current = []
        else:
            current.append(items[i])
    if current:
        result.append(current)
    return result


def chain(*funcs):
    """
    f = chain(f1, f2, f3, f4)

    is equivalent to

    f = lambda arg: f4(f3(f2(f1(arg))))
    """
    def chained(arg):
        return reduce(lambda r, f: f(r), funcs, arg)
    return chained
