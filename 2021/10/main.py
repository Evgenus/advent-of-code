def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


ERROR_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

OPENS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

CLOSES = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


def task1(filename):
    data = read_data(filename)
    score = 0
    for line in data:
        stack = []
        for char in line:
            if char in OPENS:
                stack.append(char)
            elif char in CLOSES:
                if not stack or stack[-1] != CLOSES[char]:
                    score += ERROR_POINTS[char]
                    break
                stack.pop()
    return score


COMPLETION_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def task2(filename):
    data = read_data(filename)
    scores = []
    for line in data:
        stack = []
        for char in line:
            if char in OPENS:
                stack.append(char)
            elif char in CLOSES:
                if not stack or stack[-1] != CLOSES[char]:
                    break
                stack.pop()
        else:
            score = 0
            while stack:
                score = score * 5 + COMPLETION_POINTS[OPENS[stack.pop()]]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


assert task1('test.txt') == 26397
assert task1('data.txt') == 193275
assert task2('test.txt') == 288957
assert task2('data.txt') == 2429644557
