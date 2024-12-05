from utils import *
# load_input()

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = read_data(filename)
    result = 0
    orders, updates = list_split(lines, [""])
    orders = lmap(str_tsplit('|'), orders)
    updates = lmap(str_split(','), updates)

    def is_valid(update):
        for a, b in orders:
            if a not in update:
                continue
            if b not in update:
                continue

            if not update.index(a) < update.index(b):
                return False
        return True

    for update in updates:
        if not is_valid(update):
            continue
        result += int(update[len(update) // 2])

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0
    orders, updates = list_split(lines, [""])
    orders = smap(str_tsplit('|'), orders)
    updates = lmap(str_split(','), updates)

    def is_valid(update):
        for a, b in orders:
            if a not in update:
                continue
            if b not in update:
                continue

            if not update.index(a) < update.index(b):
                return False
        return True

    @cmp_to_key
    def key(a, b):
        if (a, b) in orders:
            return -1
        if (b, a) in orders:
            return 1
        return 0

    for update in updates:
        if is_valid(update):
            continue
        update.sort(key=key)
        result += int(update[len(update) // 2])

    print(f"2: {filename}, {result}")
    return result


assert task1('test.txt') == 143
assert task1('data.txt') == 4774
assert task2('test.txt') == 123
assert task2('data.txt') == 6004
