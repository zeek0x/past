c = [[int(c) for c in input().split(' ')] for _ in range(3)]

ans = \
    c[0][0] - c[1][0] == \
    c[0][1] - c[1][1] == \
    c[0][2] - c[1][2] and \
    c[1][0] - c[2][0] == \
    c[1][1] - c[2][1] == \
    c[1][2] - c[2][2] and \
    c[0][0] - c[0][1] == \
    c[1][0] - c[1][1] == \
    c[2][0] - c[2][1] and \
    c[0][1] - c[0][2] == \
    c[1][1] - c[1][2] == \
    c[2][1] - c[2][2]

print('Yes') if ans else print('No')
