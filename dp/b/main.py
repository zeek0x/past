N, K = map(int, input().split())
H = list(map(int, input().split()))

cost = [10**20]*N

cost[0] = 0

for i in range(N):
    for j in range(1, K+1):
        if i+j < N:
            cost[i+j] = min(cost[i+j], cost[i]+abs(H[i] - H[i+j]))

print(cost[N-1])
