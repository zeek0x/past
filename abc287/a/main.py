N, M = map(int, input().split())
S = [input() for _ in range(N)]

FOR = S.count('For')
print('Yes') if FOR > N//2 else print('No')
