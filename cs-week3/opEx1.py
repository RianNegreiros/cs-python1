import math

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))
d = int(input("Digite o quarto número:"))

e = math.sqrt((a - b) ** 2) + math.sqrt((c - d) ** 2)

if e > 10:
    print("longe")
else:
    print("perto")

