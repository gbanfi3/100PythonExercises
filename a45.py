# import string
#
# for i in string.ascii_lowercase:
#     f = open("./letters2/" + i + ".txt", "w")
#     # print("letters2/" + i + ".txt")
#     f.write(i)
#     f.close()

import os

dirr = "./letters3/"
if not os.path.exists(dirr):
    os.mkdir(dirr)
