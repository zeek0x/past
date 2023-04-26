N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

color = C[0]

for i in range(N):
    if T == C[i]:
        color = C[i]
        break

max = -1
max_p = -1
for i in range(N):
    if C[i] == color and R[i] > max:
        max = R[i]
        max_p = i + 1

print(max_p)
