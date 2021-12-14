# Exercício 1

Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "**perímetro: x - área: y"**

Abaixo um exemplo de como devem ser a entrada e saída de dados do programa:

Exemplo:

  - Entrada de Dados: 

**Digite o valor correspondente ao lado de um quadrado: 3**

  - Saída de Dados:

**perímetro: 12 - área: 9**

**Dica**: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez

# Exercício 2

Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

  - Entrada de Dados:

**Digite a primeira nota: 4**

**Digite a segunda nota: 5**

**Digite a terceira nota: 6**

**Digite a quarta nota: 7**

  - Saída de Dados:

**A média aritmética é 5.5**
Dica: uso do print

Quando você usa o comando print para imprimir mais de uma coisa, ele inclui automaticamente espaços entre os argumentos impressos. Cuidado para não incluir espaços demais na sua resposta! O corretor perceberá e tirará pontos

```
>>>print("uma coisa", "outra coisa")
uma coisa outra coisa
>>>print("aqui tem ", 2, "espaços")
aqui tem  2 espaços
```

# Exercício 1 (opcional)
Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:

```
Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
```

Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, **o valor não precisa ser convertido para número**, pode ser tratado como texto.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

  - Entrada de Dados:

```
Digite o nome do cliente: Fulano de Tal
Digite o dia de vencimento: 9
Digite o mês de vencimento: Janeiro
Digite o valor da fatura: 350,00
```

 - Saída de Dados:

```
Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
```

# Exercício 2 (opcional)

Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: **a dias, b horas, c minutos e d segundos**. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

  - Entrada de Dados:

**Por favor, entre com o número de segundos que deseja converter: 178615**

  - Saída de Dados:

**2 dias, 1 horas, 36 minutos e 55 segundos.**

# Exercício 3 (opcional)

Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:

Exemplo 1:

  - Entrada de Dados:

**Digite um número inteiro: 78615**

  - Saída de Dados:

**O dígito das dezenas é 1**

Exemplo 2:

    Entrada de Dados:

Digite um número inteiro: 2

    Saída de Dados:

O dígito das dezenas é 0

Dica: O operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor. O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.