R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]


def exist(x, y):
    for r in range(R):
        for c in range(C):
            if B[r][c] == "#" or B[r][c] == ".":
                continue
            radius = int(B[r][c])
            distance = abs(x - c) + abs(y - r)
            if radius >= distance:
                return True
    return False


for r in range(R):
    for c in range(C):
        if B[r][c] == "#" and exist(c, r):
            B[r][c] = "."

for r in range(R):
    for c in range(C):
        if B[r][c] != "#":
            B[r][c] = "."

for r in range(R):
    for c in range(C):
        print(B[r][c], end="")
    print()
