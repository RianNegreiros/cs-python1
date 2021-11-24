import math
s = input("Por favor, entre com o número de segundos que deseja converter:")

days = math.floor(int(s)/86400)
d = math.floor(int(s)%86400)

hours = math.floor(int(d)/3600)
h = math.floor(int(d)%3600)

minutes = math.floor(int(h)/60)

seconds = int(s) - (minutes + hours * 60 + days * 24 * 60) * 60

print(days, "dias,", hours, "horas,", minutes, "minutos e", seconds, "segundos.")