l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))

linha = 1
coluna = 0
while linha <= a:
    print("#", end="")
    coluna = 2
    while coluna < l:
        if linha == 1 or linha == a or coluna == l:
            print("#", end="")
        else:
            print(end=" ")
        coluna += 1

    print("#")
    linha += 1
