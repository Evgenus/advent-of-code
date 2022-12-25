from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def from_snafu(number):
    s = 0
    for d in number:
        s *= 5
        if d == '-':
            s -= 1
        elif d == '=':
            s -= 2
        else:
            s += int(d)
    return s


def to_snafu(number):
    s = ''
    while number:
        d = number % 5
        number //= 5
        if d <= 2:
            s = str(d) + s
        else:
            number += 1
            d -= 5
            if d == -1:
                s = '-' + s
            else:
                s = '=' + s
    return s


def task1(filename):
    numbers = read_data(filename)
    s = sum(
        from_snafu(number)
        for number in numbers
    )
    return to_snafu(s)


CASES = [
    ('1', 1),
    ('1-', 4),
    ('1-0', 20),
    ('1-0---0', 12345),
    ('1-12', 107),
    ('10', 5),
    ('11', 6),
    ('111', 31),
    ('112', 32),
    ('1121-1110-1=0', 314159265),
    ('12', 7),
    ('12111', 906),
    ('122', 37),
    ('1=', 3),
    ('1=-0-2', 1747),
    ('1=-1=', 353),
    ('1=0', 15),
    ('1=11-2', 2022),
    ('2', 2),
    ('2-', 9),
    ('20', 10),
    ('20012', 1257),
    ('21', 11),
    ('2=', 8),
    ('2=01', 201),
    ('2=0=', 198),
]


def tests():
    for snafu, number in CASES:
        assert from_snafu(snafu) == number
        assert to_snafu(number) == snafu


tests()

assert task1('test.txt') == '2=-1=0'
assert task1('data.txt') == '2=--00--0220-0-21==1'
