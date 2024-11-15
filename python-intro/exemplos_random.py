import random

print(random.random()) # Número randomico
print(random.randint(1, 10))  # Número randomico em uma faixa
print(random.randrange(1, 10, 2)) # Número randomico em uma faixa par
print(random.randrange(1, 10, 3)) # Número randomico em uma faixa impar

x = ['K', 'd' , 13, '34' , 'x']

print(random.choice(x)) # Sotear um elemento de uma lista