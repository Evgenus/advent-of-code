from utils import *
from operator import add, sub, mul, truediv


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    values = {}
    expressions = {}
    for line in data.strip().splitlines():
        name, expr = line.split(': ')
        if expr.isnumeric():
            expr = int(expr)
            values[name] = expr
        else:
            a, op, b = expr.split(' ')
            expressions[name] = [a, op, b]

    return values, expressions


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}


def calculate(name, values, expressions):
    def calc(n):
        if n not in values:
            a, op, b = expressions[n]
            values[n] = OPERATORS[op](calc(a), calc(b))
        return values[n]
    return calc(name)


def task1(filename):
    values, expressions = read_data(filename)
    return calculate('root', values, expressions)


def task2(filename):
    values, expressions = read_data(filename)

    expressions['root'][1] = '-'  # change root operation to subtraction

    def func(x):
        return calculate('root', {**values, 'humn': x}, expressions)

    dx = 1
    x = values['humn']
    m = sign(func(x + dx) - func(x))  # function is increasing or decreasing
    # search such `x` that `func(x) == 0`
    while True:
        while True:
            y = func(x)
            if y == 0:
                return x
            if y * dx * m > 0:
                # we flipped over zero point, lets go another direction
                break
            x += dx  # moving towards zero point
            dx *= 2  # increasing speed
        dx = -sign(dx)
        x += dx


assert task1('test.txt') == 152
assert task1('data.txt') == 63119856257960
assert task2('test.txt') == 301
assert task2('data.txt') == 3006709232464
