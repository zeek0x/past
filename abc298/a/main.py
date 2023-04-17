N = int(input())
S = input()

good = 'o' in S
impossible = 'x' in S

print('Yes') if good and not impossible else print('No')
