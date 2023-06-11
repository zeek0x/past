from collections import defaultdict

S = input()

n = 0
d = defaultdict(int)
d[0] += 1
for s in S:
    n = n ^ (1 << int(s))
    d[n] += 1


ans = 0
for v in d.values():
    ans += v * (v - 1) // 2

print(ans)
