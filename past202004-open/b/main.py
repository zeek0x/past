s = input()
o = {}
for c in s:
    if c in o:
        o[c] += 1
    else:
        o[c] = 1
mk, mv = '', 0
for k, v in o.items():
    if mv < v:
        mk = k
        mv = v
print(mk)
