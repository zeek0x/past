N = int(input())
S = input()

for i in range(1, N):
    l = 0
    for j in range(0, N-i):
        if S[j] != S[i+j]:
            l += 1
        else:
            break
    print(l)
