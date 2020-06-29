a=['1', 1, '1', 2]

b = []
for i in a:
    if not i in b:
        b.append(i)
print(b)

c = set(a)
print(c)


