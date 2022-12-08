with open('data.txt', 'r') as f:
    data = f.read()

matrix = []

for line in data.strip().splitlines():
    matrix.append([int(x) for x in line])


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


def get_score(i, j, func):
    score = 1
    tree = matrix[i][j]
    score *= func(tree, [matrix[i][k] for k in range(j + 1, len(matrix))])  # right
    score *= func(tree, [matrix[i][k] for k in range(j - 1, -1, -1)])  # left
    score *= func(tree, [matrix[k][j] for k in range(i + 1, len(matrix))])  # down
    score *= func(tree, [matrix[k][j] for k in range(i - 1, -1, -1)])  # up
    return score


def task1():
    return sum(
        get_score(i, j, is_hidden) == 0
        for i in range(0, len(matrix))
        for j in range(0, len(matrix))
    )


def task2():
    return max(
        get_score(i, j, max_index)
        for i in range(0, len(matrix))
        for j in range(0, len(matrix))
    )


print(task1())
print(task2())
