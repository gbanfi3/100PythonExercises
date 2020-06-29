def vel(v1, v2, t1, t2):
    if t1 == t2:
        return -1
    else:
        return (v2-v1)/(t2-t1)

print(vel(0,10,0,20))