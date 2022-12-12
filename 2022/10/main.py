def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def gen_stream(filename):
    lines = read_data(filename)
    value = 1
    for line in lines:
        if line.startswith('noop'):
            yield value
        elif line.startswith('addx'):
            yield value
            yield value
            _, v = line.split()
            value += int(v)


def task1(filename):
    cycles = [
        20, 60, 100, 140, 180, 220
    ]

    res = 0
    value = 1

    stream = gen_stream(filename)
    start = 0
    for end in cycles:
        for _ in range(start, end):
            value = next(stream, value)
        res += value * end
        start = end
    return res


def task2(filename):
    s = gen_stream(filename)
    for y in range(6):
        for x in range(40):
            value = next(s)
            print('.#'[value - 1 <= x <= value + 1], end='')
        print()


assert task1('test.txt') == 13140
assert task1('data.txt') == 13760
task2('data.txt')
