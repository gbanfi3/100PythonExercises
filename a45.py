import string

for i in string.ascii_lowercase:
    f = open("/letters2/" + i + ".txt", "w")
    f.write(i)
    f.close()
