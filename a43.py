import string

a = string.ascii_lowercase
with open("a43.txt", "w") as file:
    hossz = len(a)
    if hossz % 2:
        a += " "
        hossz = len(a)
    for n in range(int(hossz/2)):
        file.write(a[2*n] + a[2*n+1] + "\n")

