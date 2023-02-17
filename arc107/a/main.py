A, B, C = map(int, input().split())

N = A * (A+1) * B * (B+1) * C * (C+1) // 8

print(N % 998244353)
