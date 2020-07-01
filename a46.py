import sys, os, pprint
dirr = "letters3"
if not os.path.exists(dirr):
    sys.exit(1)
files = os.listdir(dirr)
# pprint.pprint(files)
c = []
for f in files:
    # f2 = "\\" + dirr + "\\" + f
    # x = r"alma\\" + dirr
    with open(dirr + "/" + f, 'r') as ff:
        a = ff.read()
        c.append(a)
pprint.pprint(c)
