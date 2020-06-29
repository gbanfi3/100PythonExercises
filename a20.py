d = {"a": 1, "b": 2, "c": 3}
summ = 0
for i in d:
    summ += d[i]
print(summ)

a = sum([d[i] for i in d])
print(a)

b = 0
for i in d.keys():
    b += d[i]
print(b)

b = 0
for i in d.values():
    b += i
print(b)

c= sum(d.values())
print(c)
