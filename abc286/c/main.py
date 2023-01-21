N, A, B = map(int, input().split())
S = input()

ans = B * N

for i in range(N):
    s = S[i:] + S[:i]
    n = i * A

    for j in range(int(N/2)):
        if s[j] != s[N-1-j]:
            n += B

    if ans > n:
        ans = n

print(ans)
