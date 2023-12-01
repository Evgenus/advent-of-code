from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task1(filename):
    lines = read_data(filename)
    result = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        result += int(digits[0] + digits[-1])
    return result


trans = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def find_first(line: str):
    digits = []
    for digit in list(trans.values()) + list(trans.keys()):
        index = line.find(digit)
        if index < 0:
            continue
        digits.append((index, digit))
    digits.sort()
    first = digits[0][1]
    return trans.get(first, first)


def find_last(line: str):
    digits = []
    for digit in list(trans.values()) + list(trans.keys()):
        index = line.rfind(digit)
        if index < 0:
            continue
        digits.append((index, digit))
    digits.sort()
    last = digits[-1][1]
    return trans.get(last, last)


def task2(filename):
    lines = read_data(filename)
    result = 0
    for line in lines:
        result += int(find_first(line) + find_last(line))
    return result


assert task1('test1.txt') == 142
assert task1('data.txt') == 55386
assert task2('test2.txt') == 281
assert task2('data.txt') == 54824
