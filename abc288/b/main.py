N, K = map(int, input().split())
S = [input() for _ in range(N)]
[print(s) for s in sorted(S[:K])]
