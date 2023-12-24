from itertools import combinations
from sympy import Symbol, Eq, solve

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    hails = []
    for line in lines:
        pos, speed = line.split(' @ ')
        px, py, pz = lmap(int, pos.split(', '))
        vx, vy, vz = lmap(int, speed.split(', '))
        p = (px, py, pz)
        v = (vx, vy, vz)
        hails.append((p, v))
    return hails


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def task1(filename, start, end):
    hails = read_data(filename)

    hails = [
        ((px, py, pz), (px + vx, py + vy, pz + vz))
        for (px, py, pz), (vx, vy, vz) in hails
    ]

    result = 0
    for a, b in combinations(hails, 2):
        intersection = line_intersection(a, b)
        if intersection is None:
            continue
        x, y = intersection
        if not (start <= x <= end and start <= y <= end):
            continue
        t1 = (x - a[0][0]) / (a[1][0] - a[0][0])
        t2 = (x - b[0][0]) / (b[1][0] - b[0][0])
        if t1 > 0 and t2 > 0:
            result += 1
    return result


def task2(filename):
    hails = read_data(filename)

    hails = hails[:3]
    times = [Symbol(f't{i}') for i, _ in enumerate(hails)]

    rock_px = Symbol(f'rock_px')
    rock_py = Symbol(f'rock_py')
    rock_pz = Symbol(f'rock_pz')
    rock_vx = Symbol(f'rock_vx')
    rock_vy = Symbol(f'rock_vy')
    rock_vz = Symbol(f'rock_vz')
    params = [rock_px, rock_py, rock_pz, rock_vx, rock_vy, rock_vz]

    equations = []
    for t, ((px, py, pz), (vx, vy, vz)) in zip(times, hails):
        equation = Eq(px + vx * t, rock_px + rock_vx * t)
        equations.append(equation)
        equation = Eq(py + vy * t, rock_py + rock_vy * t)
        equations.append(equation)
        equation = Eq(pz + vz * t, rock_pz + rock_vz * t)
        equations.append(equation)

    results = solve(equations, times + params, dict=True)
    assert len(results) == 1
    result = results[0]
    return result[rock_px] + result[rock_py] + result[rock_pz]


assert task1('test.txt', 7, 27) == 2
assert task1('data.txt', 200000000000000, 400000000000000) == 15107
assert task2('test.txt') == 47
assert task2('data.txt') == 856642398547748
