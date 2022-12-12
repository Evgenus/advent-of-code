from collections import Counter


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    sizes = Counter()
    current = []

    for line in data.strip().splitlines():
        if line.startswith('$ cd'):
            name = line.split()[2]
            if name == '..':
                current.pop()
            else:
                current.append(name)
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            pass
        else:
            size = int(line.split()[0])
            for i in range(len(current), 0, -1):
                sizes['/'.join(current[:i])] += size

    return sizes


def task1(filename):
    sizes = read_data(filename)

    res = 0
    for path, len in sizes.items():
        if len > 100000:
            continue
        res += len

    return res


def task2(filename):
    sizes = read_data(filename)

    size = 70000000 - sizes['/']

    for s in sorted(sizes.values()):
        if s >= 30000000 - size:
            return s


assert task1('test.txt') == 95437
assert task2('test.txt') == 24933642
assert task1('data.txt') == 1447046
assert task2('data.txt') == 578710
