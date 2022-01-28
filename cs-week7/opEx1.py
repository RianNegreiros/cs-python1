def n_primos(n):
    if n == 2:
        return 1
    p = 0
    for i in range(2, n):
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            p += 1
    return p


print(n_primos(2))
