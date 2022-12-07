with open('data.txt', 'r') as stream:
    data = stream.read()

intervals = []
for line in data.strip().splitlines():
    a, b = line.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    intervals.append((a1, a2, b1, b2))

res = 0
for a1, a2, b1, b2 in intervals:
    if a1 <= b1 and b2 <= a2:
        res += 1
    elif b1 <= a1 and a2 <= b2:
        res += 1
print(res)

res = 0
for a1, a2, b1, b2 in intervals:
    res += a1 <= b1 <= a2 or b1 <= a1 <= b2
print(res)
