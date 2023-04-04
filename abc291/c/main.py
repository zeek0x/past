N = int(input())
S = input()

ok = False
x, y = (0, 0)

hist = set()
hist.add((x, y))

for s in S:
    if s == 'L':
        x += 1
    elif s == 'R':
        x -= 1
    elif s == 'U':
        y += 1
    elif s == 'D':
        y -= 1

    if (x, y) in hist:
        ok = True
        break
    hist.add((x, y))

print('Yes') if ok else print('No')
