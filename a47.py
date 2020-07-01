import glob

files = glob.glob("letters3/*.txt")
aa = []
for f in files:
    with open(f, "r") as ff:
        c = ff.read()
        if c in "python":
            aa.append(c)
print(c)