N = int(input())
S = input()
T = input()

ok = True
for i in range(N):
    s = S[i]
    t = T[i]
    if s == t:
        continue
    if s == 'l' and t == '1':
        continue
    if s == '1' and t == 'l':
        continue
    if s == '0' and t == 'o':
        continue
    if s == 'o' and t == '0':
        continue
    ok = False
    break

print('Yes') if ok else print('No')
