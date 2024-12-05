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
    orders = [order.split('|') for order in orders]
    for update in updates:
        update = update.split(',')
        if all(update.index(a) < update.index(b) for a, b in orders if a in update and b in update):
            result += int(update[len(update) // 2])

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0
    orders, updates = list_split(lines, [""])
    orders = {tuple(order.split('|')) for order in orders}
    for update in updates:
        update = update.split(',')
        if not all(update.index(a) < update.index(b) for a, b in orders if a in update and b in update):
            update.sort(key=cmp_to_key(lambda a, b: -1 if (a, b) in orders else 1 if (b, a) in orders else 0))
            result += int(update[len(update) // 2])

    print(f"2: {filename}, {result}")
    return result


assert task1('test.txt') == 143
assert task1('data.txt') == 4774
assert task2('test.txt') == 123
assert task2('data.txt') == 6004
