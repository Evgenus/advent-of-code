with open('data.txt', 'r') as f:
    data = f.read()


def gen_stream():
    value = 1
    for line in data.strip().splitlines():
        if line.startswith('noop'):
            yield value
        elif line.startswith('addx'):
            yield value
            yield value
            _, v = line.split()
            value += int(v)


def task1():
    cycles = [
        20, 60, 100, 140, 180, 220
    ]

    res = 0
    value = 1

    stream = gen_stream()
    start = 0
    for end in cycles:
        for _ in range(start, end):
            value = next(stream, value)
        res += value * end
        start = end
    return res


def task2():
    s = gen_stream()
    for y in range(6):
        for x in range(40):
            value = next(s)
            print('.#'[value - 1 <= x <= value + 1], end='')
        print()


print(task1())
task2()
