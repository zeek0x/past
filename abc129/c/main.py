N, M = map(int, input().split())

ok = [True]*(N+1)
for i in range(M):
    a = int(input())
    ok[a] = False

MOD = 10**9+7

cnt = [0]*(N+1)
cnt[0] = 1
if ok[1]:
    cnt[1] = cnt[0]

for i in range(2, N+1):
    if ok[i]:
        cnt[i] = (cnt[i-1] + cnt[i-2]) % MOD

print(cnt[N])
