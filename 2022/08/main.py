def is_hidden(target, lst):
    for k in range(0, len(lst)):
        if lst[k] >= target:
            return 1
    return 0


def max_index(target, lst):
    for k in range(0, len(lst)):
        if lst[k] >= target:
            return k + 1
    return max(len(lst), 1)


def get_score(matrix, i, j, func):
    score = 1
    tree = matrix[i][j]
    score *= func(tree, [matrix[i][k] for k in range(j + 1, len(matrix[i]))])  # right
    score *= func(tree, [matrix[i][k] for k in range(j - 1, -1, -1)])  # left
    score *= func(tree, [matrix[k][j] for k in range(i + 1, len(matrix))])  # down
    score *= func(tree, [matrix[k][j] for k in range(i - 1, -1, -1)])  # up
    return score


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return [
        [int(x) for x in line]
        for line in data.strip().splitlines()
    ]


def task1(filename):
    matrix = read_data(filename)
    return sum(
        get_score(matrix, i, j, is_hidden) == 0
        for i in range(0, len(matrix))
        for j in range(0, len(matrix[i]))
    )


def task2(filename):
    matrix = read_data(filename)
    return max(
        get_score(matrix, i, j, max_index)
        for i in range(0, len(matrix))
        for j in range(0, len(matrix[i]))
    )


assert task1("test.txt") == 21
assert task2("test.txt") == 16
assert task1("data.txt") == 1829
assert task2("data.txt") == 291840
