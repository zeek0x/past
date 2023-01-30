N, W = map(int, input().split())
ws, vs = [], []
for _ in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

value = [[0 for _ in range(W+1)] for _ in range(N)]
value[0][0] = 0

for i in range(N):
    for w in range(W+1):
        value[i][w] = max(value[i][w], value[i-1][w])
        if w - ws[i] >= 0:
            value[i][w] = max(value[i][w], value[i-1][w-ws[i]] + vs[i])

ans = max(value[N-1])
print(ans)
