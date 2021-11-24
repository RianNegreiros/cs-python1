n = int(input("Digite um número:"))

i = 0

while n > 0:
  r = n%10
  n = n//10
  i +=r
print(i)