N = int(input())
S = input()

ok = True

for i in range(N-1):
    if S[i] == S[i+1]:
        ok = False
        break

print('Yes') if ok else print('No')
