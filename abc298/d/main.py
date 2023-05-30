from collections import deque

MOD = 998244353
Q = int(input())
S = deque()
S.append(1)
ans = 1
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        S.append(x)
        ans = (ans * 10 + x) % MOD
    elif query[0] == '2':
        x = S.popleft()
        ans -= x * pow(10, len(S), MOD)
    elif query[0] == '3':
        print(ans % MOD)
