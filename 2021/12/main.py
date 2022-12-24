from collections import (
    Counter,
    defaultdict,
)


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    links = defaultdict(list)
    for line in data.strip().splitlines():
        a, b = line.split('-')
        links[a].append(b)
        links[b].append(a)

    return links


def task1(filename):
    links = read_data(filename)

    def dfs(node, visited):
        if node == 'end':
            return 1
        if node[0].islower():
            visited.add(node)
        result = sum(
            dfs(n, visited) for n in links[node]
            if n not in visited
        )
        if node[0].islower():
            visited.remove(node)
        return result

    return dfs('start', set())


def task2(filename):
    links = read_data(filename)

    def dfs(node, visited, cap):
        if node == 'end':
            return 1
        if node[0].islower():
            visited[node] += 1
        result = sum(
            dfs(n, visited, cap or visited[n]) for n in links[node]
            if visited[n] < (2 - cap)
        )
        if node[0].islower():
            visited[node] -= 1
        return result

    c = Counter()
    c['start'] = 2
    return dfs('start', c, False)


assert task1('test1.txt') == 10
assert task1('test2.txt') == 19
assert task1('test3.txt') == 226
assert task1('data.txt') == 4104
assert task2('test1.txt') == 36
assert task2('test2.txt') == 103
assert task2('test3.txt') == 3509
assert task2('data.txt') == 119760
