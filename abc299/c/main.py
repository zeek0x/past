N = int(input())
S = input()

L = 0
l = 0
hasBar = False
for i in range(N):
    if S[i] == 'o':
        l += 1
    else:
        if l > L:
            L = l
        l = 0
        hasBar = True

if hasBar:
    if l > L:
        L = l

print(L) if L != 0 else print(-1)
