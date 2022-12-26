import json

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(json.loads, data.strip().splitlines())


class Leaf:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Leaf({self.value})"

    def add(self, other):
        self.value += other.value


def flat(root):
    for node in root:
        if isinstance(node, list):
            yield from flat(node)
        else:
            yield node


def replace(root, node, value):
    for i, child in enumerate(root):
        if child is node:
            root[i] = value
            return True
        elif isinstance(child, list):
            if replace(child, node, value):
                return True
    return False


def pairs_depth(root, depth=0):
    for node in root:
        if isinstance(node, list):
            yield from pairs_depth(node, depth + 1)

    if all(isinstance(node, Leaf) for node in root):
        yield root, depth


def wrap(root):
    nodes = []
    for node in root:
        if isinstance(node, list):
            nodes.append(wrap(node))
        else:
            nodes.append(Leaf(node))
    return nodes


def unwrap(root):
    nodes = []
    for node in root:
        if isinstance(node, list):
            nodes.append(unwrap(node))
        else:
            nodes.append(node.value)
    return nodes


def explode(tree):
    flattened = list(flat(tree))
    for pair, depth in pairs_depth(tree):
        if depth >= 4:
            regular_left = flattened.index(pair[0]) - 1
            if regular_left >= 0:
                flattened[regular_left].add(pair[0])

            regular_right = flattened.index(pair[1]) + 1
            if regular_right < len(flattened):
                flattened[regular_right].add(pair[1])

            replace(tree, pair, Leaf(0))
            return True

    return False


def split(tree):
    flattened = list(flat(tree))
    for node in flattened:
        if node.value >= 10:
            a = Leaf(node.value // 2)
            b = Leaf(node.value - node.value // 2)
            replace(tree, node, [a, b])
            return True
    return False


def addition(a, b):
    tree = [a, b]
    while True:
        performed = False
        while explode(tree):
            performed = True
        if split(tree):
            performed = True
        if not performed:
            break
    return tree


def magnitude(tree):
    if isinstance(tree, Leaf):
        return tree.value
    a, b = tree
    return 3 * magnitude(a) + 2 * magnitude(b)


EXPLODE_CASES = [
    ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4]),
    ([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]]),
    ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
    ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]),
    ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]),
]

SPLIT_CASES = [
    ([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]),
    ([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]], [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]),
]

MAGNITUDE_CASES = [
    ([[1, 2], [[3, 4], 5]], 143),
    ([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384),
    ([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 445),
    ([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 791),
    ([[[[5, 0], [7, 4]], [5, 5]], [6, 6]], 1137),
    ([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488),
]


def test():
    for case, expected in EXPLODE_CASES:
        wrapped = wrap(case)
        explode(wrapped)
        unwrapped = unwrap(wrapped)
        assert unwrapped == expected

    for case, expected in SPLIT_CASES:
        wrapped = wrap(case)
        split(wrapped)
        unwrapped = unwrap(wrapped)
        assert unwrapped == expected

    a = wrap([[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
    b = wrap([1, 1])
    c = addition(a, b)
    assert unwrap(c) == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]

    for case, expected in MAGNITUDE_CASES:
        wrapped = wrap(case)
        assert magnitude(wrapped) == expected


def task1(filename):
    data = lmap(wrap, read_data(filename))
    result = data[0]
    for tree in data[1:]:
        result = addition(result, tree)
    return magnitude(result)


def task2(filename):
    data = read_data(filename)
    result = 0
    for a in data:
        for b in data:
            if a is b:
                continue
            result = max(result, magnitude(addition(wrap(a), wrap(b))))
    return result


test()


assert task1('test.txt') == 4140
assert task1('data.txt') == 3665
assert task2('test.txt') == 3993
assert task2('data.txt') == 4775
