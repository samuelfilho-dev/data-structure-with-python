tempo_gasto = float(input('Qual tempo gasto na viagem (h)? '))
velocidade_media = float(input('Qual Sua Velocidade Média (Km/h)? '))

distancia = tempo_gasto * velocidade_media

## automóvel que faz 12 Km por litro.
litros_usados = distancia / 12

print('#' * 20)
print(f'Velocidade Média: {velocidade_media}')
print(f'Tempo Gasto Na Viagem: {tempo_gasto}')
print(f'Distância Pecorrida: {distancia}')
print(f'Litros Usados Na Viagem: {round(litros_usados)}')
print('#' * 20)