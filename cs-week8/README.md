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