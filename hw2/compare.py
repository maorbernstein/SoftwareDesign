def compare(a,b):
    x = int(a)
    y = int(b)
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

print compare(1,0)
print compare(0,1)
print compare(0,0)
