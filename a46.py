import os, pprint
dirr = "letters3"
if os.path.exists(dirr):
    files = os.listdir(dirr)
    pprint.pprint(files)
