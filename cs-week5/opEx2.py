def maximo(a, b, c):
    if a >= b:
        return a
    elif a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
