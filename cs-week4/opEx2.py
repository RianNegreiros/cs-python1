n = str(input("Digite um número inteiro: "))

for index, num in enumerate(n):
    if index == len(n) - 1:
        print("nao")
        break

    nextNum = index + 1
    if num == n[nextNum]:
        print("sim")
        break
