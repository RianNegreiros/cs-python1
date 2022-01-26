n = 0
while n < 2:
    n = int(input("Digite um número: "))

for i in range(2, n):
    if n % i == 0:
        print("não primo")
        break
    else:
        print("primo")
        break
