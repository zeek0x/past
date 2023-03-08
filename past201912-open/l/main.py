import heapq
import math

N, M = map(int, input().split())
xyc_large = [list(map(int, input().split())) for _ in range(N)]
xyc_small = [list(map(int, input().split())) for _ in range(M)]


def has_bit(n, i):
    return (n & (1 << i) > 0)


def calc_edge_cost(xyc1, xyc2):
    x1, y1, c1 = xyc1
    x2, y2, c2 = xyc2
    cost = math.hypot(x1-x2, y1-y2)
    if c1 != c2:
        cost *= 10
    return cost


ans = 10.0 ** 100

for b in range(1 << M):
    xyc_use = [xyc for xyc in xyc_large]
    xyc_use += [xyc_small[i] for i in range(M) if has_bit(b, i)]
    sz = len(xyc_use)

    Q = []
    heapq.heapify(Q)
    used = [False]*sz
    Q.append([0.0, 0])
    res = 0.0
    while len(Q):
        cost, i = heapq.heappop(Q)
        if used[i]:
            continue

        res += cost
        used[i] = True
        for j in range(sz):
            if used[j]:
                continue

            cost = calc_edge_cost(xyc_use[i], xyc_use[j])
            heapq.heappush(Q, [cost, j])

    ans = min(ans, res)

print('{:.12f}'.format(ans))
