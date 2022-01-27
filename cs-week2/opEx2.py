import math

s = int(input("Por favor, entre com o número de segundos que deseja converter:"))

days = math.floor(s / 86400)
d = math.floor(s % 86400)

hours = math.floor(d / 3600)
h = math.floor(d % 3600)

minutes = math.floor(h / 60)

seconds = s - (minutes + hours * 60 + days * 24 * 60) * 60

print(days, "dias,", hours, "horas,", minutes, "minutos e", seconds, "segundos.")
