from string import ascii_uppercase

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

table = '.' + ascii_uppercase

for i in range(H):
    for j in range(W):
        print(table[A[i][j]], end='')
    print()
