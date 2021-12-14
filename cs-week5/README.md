# Exercício 1 - Máximo

Escreva a função **maximo** que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Exemplos de execução no shell do Python:

```
>>> maximo(3, 4)
4
>>> maximo(0, -1)
0
```

# Exercício 2 - Primos

Escreva a função **maior_primo** que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:

```
>>> maior_primo(100)
97
>>> maior_primo(7)
7
```

**Dica**: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

# Exercício 3 - Vogais

Escreva a função **vogal** que recebe um único caractere como parâmetro e devolve **True** se ele for uma vogal e **False** se for uma consoante.

Exemplos de execução no shell de Python

```
>>> vogal("a")
True
>>> vogal("b")
False
>>> vogal("E")
True
```

Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

**Dica**: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.