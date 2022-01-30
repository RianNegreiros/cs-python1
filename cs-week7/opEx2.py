from math import sqrt


def e_hipotenusa(n):
    while n % 2 == 0:
        n = n // 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            if (i - 1) % 4 == 0:
                return True

            while n % i == 0:
                n = n // i

    if n > 2 and (n - 1) % 4 == 0:
        return True

    else:
        return False


def soma_hipotenusas(n):
    j = 0
    for i in range(1, n + 1):
        if e_hipotenusa(i):
            j = j + i
    return j

