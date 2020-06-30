
def countwords(f:str):
    fi = open(f, mode="r")
    alma = fi.read()
    fi.close()
    return len(alma.split())

def countwords2(f:str):
    with open(f, mode="r") as fi:
        a = fi.read()
    return len(a.split())


print(countwords("words1.txt"))
print(countwords2("words1.txt"))