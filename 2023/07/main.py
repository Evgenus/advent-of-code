from collections import defaultdict, Counter
from functools import cache, partial, cmp_to_key

from utils import *
load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


CARDS1 = "AKQJT98765432"[::-1]
CARDS2 = "AKQT98765432J"[::-1]


def to_value1(hand):
    return tuple(CARDS1.index(card) for card in hand)


def to_value2(hand):
    return tuple(CARDS2.index(card) for card in hand)


def has_five(hand):
    return Counter(Counter(hand).values())[5] == 1


def has_four(hand):
    return Counter(Counter(hand).values())[4] == 1


def has_full_house(hand):
    return Counter(Counter(hand).values())[3] == 1 and Counter(Counter(hand).values())[2] == 1


def has_three(hand):
    return Counter(Counter(hand).values())[3] == 1


def has_two_pairs(hand):
    return Counter(Counter(hand).values())[2] == 2


def has_one_pairs(hand):
    return Counter(Counter(hand).values())[2] == 1


def has_high_cards(hand):
    return Counter(Counter(hand).values())[1] == 5


@cache
def get_rank(hand):
    rank = 7
    for func in (has_five, has_four, has_full_house, has_three, has_two_pairs, has_one_pairs, has_high_cards):
        if func(hand):
            return rank
        rank -= 1
    return rank


@cache
def find_rank(hand):
    return max(get_rank(hand.replace('J', repl)) for repl in CARDS2)


def compare1(hand1, hand2):
    rank1 = get_rank(hand1)
    rank2 = get_rank(hand2)
    if rank1 < rank2:
        return -1
    if rank1 > rank2:
        return 1

    value1 = to_value1(hand1)
    value2 = to_value1(hand2)
    if value1 < value2:
        return -1
    if value1 > value2:
        return 1

    return 0


def compare2(hand1, hand2):
    rank1 = find_rank(hand1)
    rank2 = find_rank(hand2)
    if rank1 < rank2:
        return -1
    if rank1 > rank2:
        return 1

    value1 = to_value2(hand1)
    value2 = to_value2(hand2)
    if value1 < value2:
        return -1
    if value1 > value2:
        return 1

    return 0


def task1(filename):
    lines = read_data(filename)
    data = dict(lmap(str.split, lines))
    sorted_data = sorted(data.keys(), key=cmp_to_key(compare1))

    return sum(
        number * int(data[card])
        for number, card in enumerate(sorted_data, start=1)
    )


def task2(filename):
    lines = read_data(filename)
    data = dict(lmap(str.split, lines))
    sorted_data = sorted(data.keys(), key=cmp_to_key(compare2))

    return sum(
        number * int(data[card])
        for number, card in enumerate(sorted_data, start=1)
    )


assert task1('test.txt') == 6440
assert task1('data.txt') == 251136060
assert task2('test.txt') == 5905
assert task2('data.txt') == 249400220
