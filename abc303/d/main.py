X, Y, Z = map(int, input().split())
S = input()
N = len(S)
OFF = [0] * (N + 1)
ON = [0] * (N + 1)

ON[0] = 10**15

for i in range(1, N + 1):
    s = S[i - 1]
    if s == "a":
        OFF[i] = min(OFF[i - 1] + X, ON[i - 1] + Z + X)
        ON[i] = min(ON[i - 1] + Y, OFF[i - 1] + Z + Y)
    else:
        ON[i] = min(ON[i - 1] + X, OFF[i - 1] + Z + X)
        OFF[i] = min(OFF[i - 1] + Y, ON[i - 1] + Z + Y)

print(min(OFF[N], ON[N]))
