import sys, os, pprint

def mylen(a):
    return len(a)

dirr = "letters3"
if not os.path.exists(dirr):
    sys.exit(1)
files = os.listdir(dirr)
files.sort()

# c = []
# for f in files:
#     with open(dirr + "/" + f, 'r') as ff:
#         a = ff.read()
#         c.append(a)
# pprint.pprint(c)

import glob
files2 = glob.glob("letters3/*.txt")
# pprint.pprint(files2)
c=[]
for f in files2:
    with open(f) as ff:
        c.append(ff.read())
c.sort()
pprint.pprint(c)