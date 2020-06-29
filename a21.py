d = {"a": 1, "b": 2, "c": 3}

c = {}
for i in d:
    if d[i] <= 1:
        c[i] = d[i]
print(c)

for i in d:
    if d[i] > 1:
        del d[i]
print(d)