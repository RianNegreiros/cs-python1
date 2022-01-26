from math import sqrt

n = 0
while n < 2:
    n = int(input("Digite um número: "))

prime = 0
for i in range(2, int(sqrt(n)) + 1):
    if (n % i) == 0:
        prime = 1
        break
if prime == 0:
    print("primo")
else:
    print("não primo")
