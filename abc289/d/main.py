N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

steps = [False for _ in range(X+1)]
steps[0] = True
available = [True for _ in range(X+1)]
for b in B:
    available[b] = False

for i in range(1, X+1):
    for a in A:
        if i < a:
            continue
        if steps[i-a] and available[i]:
            steps[i] = True

print('Yes') if steps[X] else print('No')
