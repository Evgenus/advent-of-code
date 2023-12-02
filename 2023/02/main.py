from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task1(filename):
    lines = read_data(filename)
    result = 0
    for line in lines:
        header, game = line.split(":")
        _, id_str = header.strip().split()
        id_num = int(id_str)
        try:
            for subset in game.strip().split(";"):
                game_data = {}
                for part in subset.strip().split(","):
                    count_str, color = part.split()
                    game_data[color] = int(count_str)

                assert game_data.get('red', 0) <= 12
                assert game_data.get('green', 0) <= 13
                assert game_data.get('blue', 0) <= 14
        except AssertionError:
            pass
        else:
            result += id_num
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0
    for line in lines:
        header, game = line.split(":")
        _, id_str = header.strip().split()
        red, green, blue = 0, 0, 0
        for subset in game.strip().split(";"):
            game_data = {}
            for part in subset.strip().split(","):
                count_str, color = part.split()
                game_data[color] = int(count_str)

            red = max(red, game_data.get('red', 0))
            green = max(green, game_data.get('green', 0))
            blue = max(blue, game_data.get('blue', 0))
        result += red * green * blue
    return result


assert task1('test.txt') == 8
assert task1('data.txt') == 2795
assert task2('test.txt') == 2286
assert task2('data.txt') == 75561
