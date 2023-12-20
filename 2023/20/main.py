from collections import defaultdict, Counter
from itertools import count
from math import lcm

from utils import *
# load_input()


class Module:
    def __init__(self, name: str):
        self.name = name
        self.inputs = set()
        self.outputs = set()

    def add_input(self, source):
        self.inputs.add(source)

    def add_output(self, target):
        self.outputs.add(target)

    def receive(self, source, is_high):
        return self._send(is_high)

    def _send(self, is_high):
        for target in self.outputs:
            yield self.name, target, is_high


class FlipFlop(Module):
    def __init__(self, name: str):
        super().__init__(name)
        self.is_on = False

    def receive(self, source, is_high):
        if not is_high:
            self.is_on = not self.is_on
            yield from self._send(self.is_on)


class Conjunction(Module):
    def __init__(self, name: str):
        super().__init__(name)
        self.memory = defaultdict(bool)

    def receive(self, source, is_high):
        self.memory[source] = is_high
        result = not all(self.memory[i] for i in self.inputs)
        yield from self._send(result)


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()

    modules = defaultdict(Module)
    graph = defaultdict(set)
    for line in lines:
        source, targets = line.split(' -> ')
        targets = targets.split(', ')

        if source.startswith('&'):
            module = Conjunction(source[1:])
        elif source.startswith('%'):
            module = FlipFlop(source[1:])
        else:
            module = Module(source)

        modules[module.name] = module
        graph[module.name].update(targets)

    for source, targets in graph.items():
        for target in targets:
            if target not in modules:
                modules[target] = Module(target)
            modules[target].add_input(source)
            modules[source].add_output(target)

    return modules


def task1(filename):
    modules = read_data(filename)

    counter = Counter()
    for i in range(1000):
        queue = deque()
        queue.append(('', 'broadcaster', False))
        while queue:
            prev, source, is_high = queue.popleft()
            counter[is_high] += 1
            queue.extend(modules[source].receive(prev, is_high))
    return counter[True] * counter[False]


def task2(filename):
    modules = read_data(filename)

    sender = first(modules['rx'].inputs)
    prev = {}
    periods = {}
    for i in count():
        queue = deque()
        queue.append(('', 'broadcaster', False))
        while queue:
            source, target, is_high = queue.popleft()
            if target == sender and is_high:
                if source in prev:
                    periods[source] = i - prev[source]
                    if len(periods) == len(modules[sender].inputs):
                        return lcm(*periods.values())
                prev[source] = i
            queue.extend(modules[target].receive(source, is_high))


assert task1('test.txt') == 11687500
assert task1('data.txt') == 879834312
assert task2('data.txt') == 243037165713371
