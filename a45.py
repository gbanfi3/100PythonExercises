# import string
#
# for i in string.ascii_lowercase:
#     f = open("./letters2/" + i + ".txt", "w")
#     # print("letters2/" + i + ".txt")
#     f.write(i)
#     f.close()

import os, string

dirr = "./letters3/"
if not os.path.exists(dirr):
    os.mkdir(dirr)
for c in string.ascii_letters:
    with open(dirr + c + ".txt") as f:
        f.write(c)


