with open('data.txt', 'r') as f:
    data = f.read()

matrix = []

for line in data.strip().splitlines():
    matrix.append([int(x) for x in line])


def is_hidden(target, lst):
    for i in range(0, len(lst)):
        if lst[i] >= target:
            return 1
    return 0


def max_index(target, lst):
    for i in range(0, len(lst)):
        if lst[i] >= target:
            return i + 1
    return max(len(lst), 1)


def get_score(i, j, func):
    score = 1
    tree = matrix[i][j]
    score *= func(tree, [matrix[i][k] for k in range(j + 1, len(matrix))])
    score *= func(tree, [matrix[i][k] for k in range(j - 1, -1, -1)])
    score *= func(tree, [matrix[k][j] for k in range(i + 1, len(matrix))])
    score *= func(tree, [matrix[k][j] for k in range(i - 1, -1, -1)])
    return score


res = 0
best = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if not get_score(i, j, is_hidden):
            res += 1
        best = max(best, get_score(i, j, max_index))
print(res)
print(best)
