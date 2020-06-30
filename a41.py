import string

with open("a41.txt", "w") as file:
    for c in string.ascii_letters:
        file.write(c + "\n")

