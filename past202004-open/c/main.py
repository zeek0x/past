n = int(input())
rows = [list(input()) for _ in range(n)]

for i in range(n-1, 0, -1):
    for j in range(2 * n - 1):
        if rows[i][j] == 'X':
            if j-1 > 0 and rows[i-1][j-1] == '#':
                rows[i-1][j-1] = 'X'
            if j+1 < 2 * n - 2 and rows[i-1][j+1] == '#':
                rows[i-1][j+1] = 'X'
            if rows[i-1][j] == '#':
                rows[i-1][j] = 'X'

print('\n'.join([''.join(row) for row in rows]))
