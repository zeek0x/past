import math

T = int(input())
for _ in range(T):
    n, d, k = map(int, input().split())
    g = math.gcd(n, d)
    kk = k - 1
    print(kk * g // n  + kk * d % n)
