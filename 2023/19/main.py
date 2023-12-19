from copy import copy
from dataclasses import dataclass
from functools import cache
from typing import NamedTuple

from utils import *
# load_input()


def read_data(filename, cls):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()

    rs, ps = list_split(lines, [''])

    rules = {}
    for r in rs:
        name, defs = r[:-1].split('{')
        rules[name] = defs.split(',')

    parts = []
    for part in ps:
        values = {}
        for item in part[1:-1].split(','):
            name, value = item.split('=')
            values[name] = int(value)
        parts.append(cls(**values))

    return rules, parts


class Part(NamedTuple):
    x: int
    m: int
    a: int
    s: int

    @property
    def rating(self):
        return self.x + self.m + self.a + self.s


def make_solver1(rules):
    @cache
    def run(part: Part, name: str):
        if name == 'A':
            return True
        if name == 'R':
            return False
        for rule in rules[name]:
            if ':' in rule:
                cond, target = rule.split(':')
                if '>' in cond:
                    name, value = cond.split('>')
                    if getattr(part, name) > int(value):
                        return run(part, target)
                elif '<' in cond:
                    name, value = cond.split('<')
                    if getattr(part, name) < int(value):
                        return run(part, target)
                else:
                    assert 0, rule
            else:
                return run(part, rule)
        assert 0, name
    return run


def task1(filename):
    rules, parts = read_data(filename, Part)

    run = make_solver1(rules)
    result = 0
    for part in parts:
        if run(part, 'in'):
            result += part.rating

    return result


def apply_less(r: range, value: int):
    if r.start > value:
        return range(0), r
    if r.stop > value:
        return range(r.start, value), range(value, r.stop)
    return r, range(0)


def apply_more(r: range, value: int):
    if r.stop < value:
        return range(0), r
    if r.start <= value:
        return range(value + 1, r.stop), range(r.start, value + 1)
    return r, range(0)


@dataclass
class RangePart:
    x: range
    m: range
    a: range
    s: range

    @property
    def size(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)

    def _apply(self, func, name: str, value: int):
        r = getattr(self, name)
        ra, rb = func(r, value)
        a, b = copy(self), copy(self)
        setattr(a, name, ra)
        setattr(b, name, rb)
        return a, b

    def apply_less(self, name: str, value: int):
        return self._apply(apply_less, name, value)

    def apply_more(self, name: str, value: int):
        return self._apply(apply_more, name, value)


def make_solver2(rules):
    def run(part: RangePart, name):
        if part.size == 0:
            return 0
        if name == 'A':
            return part.size
        if name == 'R':
            return 0
        result = 0
        for rule in rules[name]:
            if ':' in rule:
                cond, target = rule.split(':')
                if '>' in cond:
                    name, value = cond.split('>')
                    a, part = part.apply_more(name, int(value))
                    result += run(a, target)
                elif '<' in cond:
                    name, value = cond.split('<')
                    a, part = part.apply_less(name, int(value))
                    result += run(a, target)
                else:
                    assert 0, rule
            else:
                result += run(part, rule)
        return result
    return run


def task2(filename):
    rules, _ = read_data(filename, Part)

    part = RangePart(
        x=range(1, 4001),
        m=range(1, 4001),
        a=range(1, 4001),
        s=range(1, 4001),
    )

    run = make_solver2(rules)

    return run(part, 'in')


assert task1('test.txt') == 19114
assert task1('data.txt') == 495298
assert task2('test.txt') == 167409079868000
assert task2('data.txt') == 132186256794011
