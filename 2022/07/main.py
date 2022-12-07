from collections import Counter

with open('data.txt', 'r') as f:
    data = f.read()

sizes = Counter()
current = []

for line in data.strip().splitlines():
    if line.startswith('$ cd'):
        name = line.split()[2]
        if name == '..':
            current.pop()
        else:
            current.append(name)
    elif line.startswith('$ ls'):
        pass
    elif line.startswith('dir'):
        pass
    else:
        size = int(line.split()[0])
        for i in range(len(current), 0, -1):
            sizes['/'.join(current[:i])] += size

res = 0
for path, len in sizes.items():
    if len > 100000:
        continue
    res += len
print(res)

size = 70000000 - sizes['/']

for s in sorted(sizes.values()):
    if s >= 30000000 - size:
        print(s)
        break
