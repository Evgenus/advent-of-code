from collections import defaultdict

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def find(ranges, num):
    res = inf
    for dst, src, length in ranges:
        if src <= num < src + length:
            res = num - src + dst
    return res if res != inf else num


def task1(filename):
    lines = read_data(filename)

    seeds = lmap(int, lines[0].split(':')[1].split())
    ranges = defaultdict(list)
    for line in lines[1:]:
        if line.endswith("map:"):
            src, _, dst = line.split(" ")[0].split("-")
        elif line:
            ranges[src, dst].append(lmap(int, line.split(' ')))
    result = inf
    for seed in seeds:
        soil = find(ranges['seed', 'soil'], seed)
        fertilizer = find(ranges['soil', 'fertilizer'], soil)
        water = find(ranges['fertilizer', 'water'], fertilizer)
        light = find(ranges['water', 'light'], water)
        temperature = find(ranges['light', 'temperature'], light)
        humidity = find(ranges['temperature', 'humidity'], temperature)
        location = find(ranges['humidity', 'location'], humidity)
        result = min(result, location)
    return result


def get_overlap(a, b):
    return max(a[0], b[0]), min(a[1], b[1])


def remap_range(ranges, start, end):
    result = []
    for dst, src, length in ranges:
        overlap_start, overlap_end = get_overlap((start, end), (src, src + length - 1))
        if overlap_start > overlap_end:
            continue
        new_start = overlap_start - src + dst
        new_end = overlap_end - src + dst
        result.append((overlap_start, overlap_end, new_start, new_end))
    result.sort()
    last = start
    for s1, e1, s2, e2 in result:
        if last < s1:
            yield last, s1 - 1
        last = e1 + 1
        yield s2, e2
    if last <= end:
        yield last, end


def remap_ranges(ranges, source):
    for start, end in source:
        yield from remap_range(ranges, start, end)


def calc_length(ranges):
    return sum(end - start + 1 for start, end in ranges)


def task2(filename):
    lines = read_data(filename)

    seeds = lmap(int, lines[0].split(':')[1].split())
    ranges = defaultdict(list)
    for line in lines[1:]:
        if line.endswith("map:"):
            src, _, dst = line.split(" ")[0].split("-")
        elif line:
            ranges[src, dst].append(lmap(int, line.split(' ')))

    seed = [(start, start + length - 1) for start, length in iter_chunks(seeds, 2)]
    soil = list(remap_ranges(ranges['seed', 'soil'], seed))
    fertilizer = list(remap_ranges(ranges['soil', 'fertilizer'], soil))
    water = list(remap_ranges(ranges['fertilizer', 'water'], fertilizer))
    light = list(remap_ranges(ranges['water', 'light'], water))
    temperature = list(remap_ranges(ranges['light', 'temperature'], light))
    humidity = list(remap_ranges(ranges['temperature', 'humidity'], temperature))
    location = list(remap_ranges(ranges['humidity', 'location'], humidity))

    return min(s for s, e in location)


assert task1('test.txt') == 35
assert task1('data.txt') == 379811651
assert task2('test.txt') == 46
assert task2('data.txt') == 27992443
