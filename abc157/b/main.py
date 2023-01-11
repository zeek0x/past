a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]

for y in range(len(a)):
    for x in range(len(a[y])):
        for t in b:
            if a[y][x] == t:
                a[y][x] = 0

ans = \
    a[0][0] + a[0][1] + a[0][2] == 0 or \
    a[1][0] + a[1][1] + a[1][2] == 0 or \
    a[2][0] + a[2][1] + a[2][2] == 0 or \
    a[0][0] + a[1][0] + a[2][0] == 0 or \
    a[0][1] + a[1][1] + a[2][1] == 0 or \
    a[0][2] + a[1][2] + a[2][2] == 0 or \
    a[0][0] + a[1][1] + a[2][2] == 0 or \
    a[2][0] + a[1][1] + a[0][2] == 0

print('Yes') if ans else print('No')
