from utils import *


class Node:
    def __init__(self, value):
        self.value = value


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(chain(int, Node), data.strip().splitlines())


def mix(nodes, times):
    result = nodes.copy()
    size = len(nodes) - 1

    for _ in range(times):
        for node in nodes:
            old_position = result.index(node)
            result.pop(old_position)
            new_position = old_position + node.value
            new_position %= size
            if new_position <= 0:
                new_position += size
            result.insert(new_position, node)

    return result


def task(filename, multiplier, times):
    nodes = read_data(filename)

    for node in nodes:
        node.value *= multiplier

    mixed = mix(nodes, times)
    [zero_index] = [index for index, node in enumerate(mixed) if node.value == 0]
    size = len(mixed)

    return sum(
        mixed[(zero_index + offset) % size].value
        for offset in (1000, 2000, 3000)
    )


assert task('test.txt', 1, 1) == 3
assert task('data.txt', 1, 1) == 7153
assert task('test.txt', 811589153, 10) == 1623178306
assert task('data.txt', 811589153, 10) == 6146976244822
