from collections import (
    Counter,
    defaultdict,
)
from functools import cache

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()

    rates = {}
    links = {}
    for line in lines:
        _, valve, _, _, srate, _, _, _, _, valves = line.split(' ', 9)
        rate = int(srate.rstrip(';').split('=')[1])
        rates[valve] = rate
        links[valve] = valves.split(', ')

    return rates, links


def task1(filename, start, limit):
    rates, links = read_data(filename)

    @cache
    def dfs(valve, time, visited):
        if time <= 1:
            return 0
        res = 0
        for link in links[valve]:
            res = max(res, dfs(link, time - 1, visited))
        if valve not in visited and rates[valve] > 0:
            visited = tuple(sorted([*visited, valve]))
            res = max(res, dfs(valve, time - 1, visited) + rates[valve] * (time - 1))

        return res

    return dfs(start, limit, ())


def task2_bad(filename, start, limit):
    rates, links = read_data(filename)

    working = sum(rate > 0 for rate in rates.values())

    @cache
    def dfs(valve, evalve, time, visited):
        if time <= 1:
            return 0
        if len(visited) == working:
            return 0
        plans = []
        for link1 in links[valve]:
            for link2 in links[evalve]:
                plans.append((
                    link1, link2, 0, visited
                ))
        if valve not in visited and rates[valve] > 0:
            for link2 in links[evalve]:
                plans.append((
                    valve, link2, rates[valve] * (time - 1), tuple(sorted([*visited, valve]))
                ))
        if evalve not in visited and rates[evalve] > 0:
            for link1 in links[valve]:
                plans.append((
                    link1, evalve, rates[evalve] * (time - 1), tuple(sorted([*visited, evalve]))
                ))
        if (
                valve not in visited and rates[valve] > 0 and
                evalve not in visited and rates[evalve] > 0 and
                valve != evalve
        ):
            plans.append((
                valve, evalve, rates[valve] * (time - 1) + rates[evalve] * (time - 1),
                tuple(sorted([*visited, valve, evalve]))
            ))
        optimized = {
            (min(n1, n2), max(n1, n2), p, v)
            for n1, n2, p, v in plans
        }
        res = 0
        for i, (n1, n2, p, v) in enumerate(optimized, 1):
            res = max(res, dfs(n1, n2, time - 1, v) + p)
        return res

    return dfs(start, start, limit, ())


def task2(filename, start, limit):
    rates, links = read_data(filename)

    weighted = defaultdict(Counter)
    for i in rates:
        for j in rates:
            if i == j:
                weighted[i][j] = 0
            elif j in links[i]:
                weighted[i][j] = 1
            else:
                weighted[i][j] = inf

    for i in rates:
        for j in rates:
            if i == j:
                continue
            for k in rates:
                if k == i or k == j:
                    continue
                weighted[i][j] = min(weighted[i][j], weighted[i][k] + weighted[k][j])

    wlinks = defaultdict(dict)
    for i in rates:
        for j in rates:
            if weighted[i][j] < inf and rates[j] > 0:
                wlinks[i][j] = weighted[i][j]

    working = {valve: rate for valve, rate in rates.items() if rate > 0}

    @cache
    def dfs(player1, player2, visited):
        res = 0
        for v, rate in working.items():
            if v in visited:
                continue
            new_visited = tuple(sorted([*visited, v]))
            valve1, time1 = player1
            if v in wlinks[valve1] and time1 - wlinks[valve1][v] >= 1:
                time_left = time1 - wlinks[valve1][v] - 1
                player1_move = dfs((v, time_left), player2, new_visited) + time_left * rate
                res = max(res, player1_move)
            valve2, time2 = player2
            if v in wlinks[valve2] and time2 - wlinks[valve2][v] >= 1:
                time_left = time2 - wlinks[valve2][v] - 1
                player2_move = dfs(player1, (v, time_left), new_visited) + time_left * rate
                res = max(res, player2_move)
        return res

    return dfs((start, limit), (start, limit), ())


assert task1('test.txt', 'AA', 30) == 1651
assert task1('data.txt', 'AA', 30) == 1741
assert task2_bad('test.txt', 'AA', 26) == 1707
assert task2('test.txt', 'AA', 26) == 1707
assert task2('data.txt', 'AA', 26) == 2316
