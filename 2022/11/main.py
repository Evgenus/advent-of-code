from collections import (
    defaultdict,
    deque,
)
from math import lcm


class Monkey:
    def __init__(self):
        self.items = deque()
        self.formula = None
        self.test = None
        self.if_true = None
        self.if_false = None
        self.count = 0

    def add(self, item):
        self.items.append(item)

    def set_formula(self, formula):
        self.formula = formula

    def set_test(self, test):
        self.test = test

    def set_true(self, m):
        self.if_true = m

    def set_false(self, m):
        self.if_false = m

    def analyze(self, monkeys, div, mod):
        if not self.items:
            return
        for i in range(len(self.items)):
            item = self.items.popleft()
            self.count += 1
            item = eval(self.formula, {}, {'old': item}) // div
            if item % self.test == 0:
                monkeys[self.if_true].add(item % mod)
            else:
                monkeys[self.if_false].add(item % mod)


def read_data():
    with open('data.txt', 'r') as f:
        data = f.read()

    monkeys = defaultdict(Monkey)

    lines = data.strip().splitlines()
    for start in range(0, len(lines), 7):
        monkey_name = lines[start].split(':')[0].split()[1]
        monkey = monkeys[monkey_name]
        items = lines[start + 1].split(': ')[1].split(', ')
        for item in items:
            monkey.add(int(item))
        monkey.set_test(int(lines[start + 3].split('by')[1].strip()))
        monkey.set_true(lines[start + 4].split()[-1])
        monkey.set_false(lines[start + 5].split()[-1])
        monkey.set_formula(lines[start + 2].split('=')[1].strip())

    return monkeys


def task(rounds, div):
    monkeys = read_data()
    factor = lcm(*[monkey.test for monkey in monkeys.values()])
    for _ in range(0, rounds):
        for monkey in monkeys.values():
            monkey.analyze(monkeys, div, factor)

    counts = sorted(
        monkey.count
        for monkey in monkeys.values()
    )
    return counts[-1] * counts[-2]


print(task(20, 3))
print(task(10000, 1))
