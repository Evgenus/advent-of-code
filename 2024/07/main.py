from utils import *
from collections import Counter
from itertools import pairwise
# load_input()

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def solve1(nums):
    if len(nums) == 1:
        yield nums[0]
    else:
        *rest, last = nums
        for p in solve1(rest):
            yield p + last
            yield p * last

def task1(filename):
    lines = read_data(filename)
    result = 0

    for line in lines:
        s, nums = line.split(":")
        s = int(s)
        nums = nums.split()
        nums = lmap(int, nums)
        if any(e == s for e in solve1(nums)):
            result += s

    print(f"1: {filename}, {result}")
    return result


def solve2(nums):
    if len(nums) == 1:
        yield nums[0]
    else:
        *rest, last = nums
        for p in solve2(rest):
            yield p + last
            yield p * last
            yield int(str(p) + str(last))

def task2(filename):
    lines = read_data(filename)
    result = 0

    for line in lines:
        s, nums = line.split(":")
        s = int(s)
        nums = nums.split()
        nums = lmap(int, nums)
        if any(e == s for e in solve2(nums)):
            result += s

    print(f"2: {filename}, {result}")
    return result


assert task1('test.txt') == 3749
assert task1('data.txt') == 5702958180383
assert task2('test.txt') == 11387
assert task2('data.txt') == 92612386119138
