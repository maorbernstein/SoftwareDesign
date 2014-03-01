def dist(s,t):
    if s=="":
        return len(t)
    if t=="":
        return len(s)
    
    x = dist(s[1:],t[1:]) + (s[0]!=t[0])
    y = dist(s,t[1:]) + 1
    z = dist(s[1:],t) + 1
    return min(x,y,z)

