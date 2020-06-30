import math

def volume(hc, r=10):
    return 4 * math.pi * r**3 /3 - math.pi * hc**2 * (3*r-hc) / 3

print(volume(hc=2))
print(volume(hc=2,r=10))
print(volume(2,r=11))