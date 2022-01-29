arr = []

while True:
    n = int(input("Digite um número: "))
    if n == 0:
        arr.reverse()
        for i in arr:
            print(i)
        break
    arr.append(n)
