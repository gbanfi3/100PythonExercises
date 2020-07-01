import glob

files = glob.iglob("letters3/*.txt")
aa = []
for f in files:
    with open(f, "r") as ff:
        c = ff.read()
        if c.strip() in "python":
            aa.append(c)
print(aa)