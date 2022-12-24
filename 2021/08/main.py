from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return [
        line.split(' | ')
        for line in data.strip().splitlines()
    ]


def task1(filename):
    readings = read_data(filename)
    res = 0
    for digits, number in readings:
        number = number.split(' ')
        res += sum(
            len(digit) in (2, 3, 4, 7)
            for digit in number
        )
    return res


"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""


SEGMENTS = 'abcdefg'
DIGITS = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]


def analyze_digits(digits):
    possible_segments = {
        segment: set(SEGMENTS)
        for segment in SEGMENTS
    }

    def accept_number(number):
        for segment in SEGMENTS:
            if segment in DIGITS[number]:
                possible_segments[segment] &= set(digit)
            else:
                possible_segments[segment] -= set(digit)

    s690 = set(SEGMENTS)
    s235 = set(SEGMENTS)

    for digit in digits:
        if len(digit) == 2:  # 1
            accept_number(1)
        if len(digit) == 3:  # 7
            accept_number(7)
        if len(digit) == 4:  # 4
            accept_number(4)
        if len(digit) == 7:  # 8
            accept_number(8)
        if len(digit) == 5:  # 2, 3, 5
            s235 &= set(digit)
        if len(digit) == 6:  # 6, 9, 0
            s690 &= set(digit)

    possible_segments['a'] &= s235
    possible_segments['d'] &= s235
    possible_segments['g'] &= s235
    possible_segments['b'] -= s235
    possible_segments['c'] -= s235
    possible_segments['e'] -= s235
    possible_segments['f'] -= s235

    possible_segments['a'] &= s690
    possible_segments['b'] &= s690
    possible_segments['f'] &= s690
    possible_segments['g'] &= s690
    possible_segments['c'] -= s690
    possible_segments['d'] -= s690
    possible_segments['e'] -= s690

    translations = {}
    for i, segments in enumerate(DIGITS):
        real_segments = set()
        for segment in segments:
            real_segments.update(possible_segments[segment])
        translations[''.join(sorted(real_segments))] = str(i)

    return translations


def task2(filename):
    readings = read_data(filename)

    result = 0
    for digits, numbers in readings:
        translations = analyze_digits(digits.split(' '))
        number = int(''.join(
            translations[''.join(sorted(number_digit))]
            for number_digit in numbers.split(' ')
        ))
        result += number

    return result


assert task1('test.txt') == 26
assert task1('data.txt') == 318
assert task2('test0.txt') == 5353
assert task2('test.txt') == 61229
assert task2('data.txt') == 996280
