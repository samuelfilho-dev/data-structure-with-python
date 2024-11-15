import datetime

print(datetime.date.today()) # Mostrar Data
print(datetime.datetime.today()) # Mostrar Data e Horario

data = datetime.date(2020, 7 , 10)
print(data)
print(data.day)
print(data.month)
print(data.year)

horario = datetime.datetime(2020, 7, 10,7,30,0)
print(horario)
print(horario.hour)
print(horario.minute)
print(horario.second)