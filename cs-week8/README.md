# Exercício 1 - Removendo elementos repetidos

Escreva a função **remove_repetidos** que recebe como parâmetro uma **lista** com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma **lista** correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar **lista.sort()** ou **sorted(lista)**. Qual a diferença?

**Exemplo**: 

```
>>>lista = [2, 4, 2, 2, 3, 3, 1]
>>>remove_repetidos(lista)
[1, 2, 3, 4]
>>>remove_repetidos([1, 2, 3, 3, 3, 4])
[1, 2, 3, 4]
```

# Exercício 2 - Soma dos elementos de uma lista

Escreva a função **soma_elementos** que recebe como parâmetro uma **lista** com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

#Exercício 1 - Maior elemento de uma lista

Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

#Exercício 2 - Invertendo sequência

Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

Exemplo:

```bash
Digite um número: 1
Digite um número: 7
Digite um número: 4
Digite um número: 0

4
7
1
```