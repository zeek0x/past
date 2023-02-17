N = int(input())
S = input()

E = [0] * N
for i in range(N-2, -1, -1):
    E[i] = E[i+1] + (1 if S[i+1] == 'E' else 0)

W = [0] * N
for i in range(1, N):
    W[i] = W[i-1] + (1 if S[i-1] == 'W' else 0)

print(min([E[i] + W[i] for i in range(N)]))
