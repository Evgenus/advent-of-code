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
    for monkey in range(0, len(lines), 7):
        monkey_name = lines[monkey].split(':')[0].split()[1]
        items = lines[monkey + 1].split(': ')[1].split(', ')
        monkeys[monkey_name].set_test(int(lines[monkey + 3].split('by')[1].strip()))
        monkeys[monkey_name].set_true(lines[monkey + 4].split()[-1])
        monkeys[monkey_name].set_false(lines[monkey + 5].split()[-1])
        monkeys[monkey_name].set_formula(lines[monkey + 2].split('=')[1].strip())

        for item in items:
            monkeys[monkey_name].add(int(item))

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
