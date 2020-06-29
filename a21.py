d = {"a": 1, "b": 2, "c": 3}

c = {}
for i in d:
    if d[i] <= 1:
        c[i] = d[i]
print(c)

print({k,v for k,v in d if v <= 1})

dd = dict(d)
for i in d:
    if d[i] > 1:
        del dd[i]
print(dd)

