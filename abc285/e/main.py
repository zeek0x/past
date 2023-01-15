N = int(input())
A = list(map(int, input().split(' ')))

f = '0'+str(N)+'b'
B = [format(i, f) for i in range(pow(2, N))]

X = []
Y = []

for i in range(N):
    x = 0
    for j in range(i, i-N, -1):
        jj = j
        if jj < 0:
            jj += N

        if B[i][jj] == '0':
            X.append(j)
    y = 0
    for j in range(i, i+N, +1):
        jj = j
        if jj > N-1:
            jj -= N

        if B[i][jj] == '0':
            Y.append(j)

maxScore = 0
for i in range(N):
    score = 0
    for j in range(N):
        x, y = X[i], Y[i]
        a = min(abs(x), y)
        score += A[a]
        print(i, j, x, y, a, score)
    if maxScore < score:
        maxScore = score

print(maxScore)
