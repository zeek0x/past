N = int(input())
ps = [0] + list(map(int, input().split()))

P = sum(ps)

exist = []
for i in range(N+1):
    exist.append([False] * (P+1))


exist[0][0] = True

for i in range(1, N+1):
    for p in range(P+1):
        if exist[i-1][p]:
            exist[i][p] = True
        if p >= ps[i] and exist[i-1][p-ps[i]]:
            exist[i][p] = True

ans = 0
for p in range(P+1):
    if exist[N][p]:
        ans += 1

print(ans)
