import heapq

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

INF = 10**100


def grid_dijkstra(si, sj):
    dist = [[INF] * W for _ in range(H)]
    Q = []
    heapq.heapify(Q)
    Q.append([0, si, sj])
    while len(Q) > 0:
        d, i, j = heapq.heappop(Q)
        if d > dist[i][j]:
            continue
        for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if 0 <= i2 < H and 0 <= j2 < W and d + A[i2][j2] < dist[i2][j2]:
                dist[i2][j2] = d + A[i2][j2]
                heapq.heappush(Q, [dist[i2][j2], i2, j2])
    return dist


dist1 = grid_dijkstra(H-1, 0)
dist2 = grid_dijkstra(H-1, W-1)
dist3 = grid_dijkstra(0, W-1)

ans = INF
for i in range(H):
    for j in range(W):
        res = dist1[i][j] + dist2[i][j] + dist3[i][j] - 2*A[i][j]
        ans = min(ans, res)

print(ans)
