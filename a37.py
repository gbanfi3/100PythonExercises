def countwords(f:str):
    with open("a37.txt", mode='r') as file:
        tart = file.read()
        tart2 = tart.replace(","," ")

    return len(tart2.split())

print(countwords("a37.txt"))
print(countwords("words2.txt"))