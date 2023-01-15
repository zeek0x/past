a, b = map(int, input().split(' '))

if b / a == 2 or (b - 1) / a == 2:
    print('Yes')
else:
    print('No')
