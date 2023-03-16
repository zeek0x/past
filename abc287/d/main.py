S = input()
T = input()
SL = len(S)
TL = len(T)


def match_or_not(a, b):
    return a == b or a == '?' or b == '?'


l = 0
for i in range(TL):
    if not match_or_not(S[i], T[i]):
        break
    l += 1

r = 0
for i in range(TL):
    if not match_or_not(S[SL-i-1], T[TL-i-1]):
        break
    r += 1

for i in range(TL+1):
    print('Yes') if i <= l and TL-i <= r else print('No')
