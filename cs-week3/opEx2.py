import math

a = float(input("Digite um a:"))
b = float(input("Digite um b:"))
c = float(input("Digite um c:"))

d = b**2 - (4*a*c)
if d < 0:
  print("esta equação não possui raízes reais")
elif(d == 0):
  r1 = (-b + math.sqrt(d)) / (2*a)
  print("a raiz desta equação é", r1)
else:
  r1 = (-b + math.sqrt(d)) / (2*a)
  r2 = (-b - math.sqrt(d)) / (2*a)
  print("as raízes da equação é",r1)
  print("as raízes da equação é",r2)