def t(s):
    n = 60
    x = str(s/n**2)
    y = s/n
    y %= n
    z = str(s%n)
    return x+":"+str(y)+":"+z

h = 4000
while h != 0:
    x = t(h)
    if "0" in x:
        print x
    h -= 1000
