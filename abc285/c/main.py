S = input()
N = len(S)

A = ord('A')

ans = 0
for i in range(N):
    s = S[N-i-1]
    x = ord(s) - A + 1
    ans += x * pow(26, i)
print(ans)
