from string import ascii_lowercase

S = input()
i = 1
for s in S:
    if s in ascii_lowercase:
        i += 1
    else:
        break

print(i)
