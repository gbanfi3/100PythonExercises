import string

def countwords(s:string):
    hossz = len(s)
    if hossz == 0:
        return 0

    if s[0] in string.ascii_letters:
        c = 1
    else:
        c = 0
    for i in range(1,hossz):
        if s[i-1] not in string.ascii_letters and s[i] in string.ascii_letters:
            c +=1
    return c

# s = ""
# s = "A"
# s = "2"
# s = "aa"
# s = "a1a"
# s = "1a1"
s = "a1. a2a3a4a5"
print(countwords(s))

s2 = s.split(sep="13")
print(s2)

# print(string.whitespace)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.printable)