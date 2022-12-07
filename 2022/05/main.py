import re
from itertools import zip_longest

with open('data.txt', 'r') as stream:
    data = stream.read()

data1 = []
data2 = []
dest = data1
for line in data.splitlines():
    if line.strip() == '':
        dest = data2
    else:
        dest.append(line)

rows = zip_longest(
    *[line[1::4]
        for line in data1[:-1][::-1]
    ],
    fillvalue=' '
)

rows = [[]] + [
    [
        box
        for box in row
        if box != ' '
    ]
    for row in rows
]

for line in data2:
    move = re.findall(r'(\d+) from (\d+) to (\d+)', line)
    amount, src, dst = move[0]
    amount, src, dst = int(amount), int(src), int(dst)
    rows[dst].extend(rows[src][-amount:])  # [::-1]
    rows[src][-amount:] = []

top = [row[-1] for row in rows[1:]]
print(''.join(top))
