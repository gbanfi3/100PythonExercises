import string

a = string.ascii_lowercase
a += "  "


with open("a44.txt","w") as file:
    for i,j,k in zip(a[::3], a[1::3], a[2::3]):
        file.write(i + j+k+"\n")
