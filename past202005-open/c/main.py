A, R, N = map(int, input().split())
large = 10 ** 9

def solve(A, R, N):
    if R == 1:
        return A

    for _ in range(N-1):
        A *= R

        if A > 10 ** 9:
            return "large"

    return A

print(solve(A, R, N))
