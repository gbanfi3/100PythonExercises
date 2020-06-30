import string

with open("a41.txt", "w") as file:
    aa =
    for n in range(len(string.ascii_letters)):
        file.write(string.ascii_letters[n] + "\n")

