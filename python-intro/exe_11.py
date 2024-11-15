def ler_valores():
    tempo_gasto = float(input('Qual tempo gasto na viagem (h)? '))
    velocidade_media = float(input('Qual Sua Velocidade Média (Km/h)? '))
    return tempo_gasto, velocidade_media


def calcular_distancia(tempo_gasto, velocidade_media):
    distancia = tempo_gasto * velocidade_media
    return distancia


def calcular_litros(distancia):
    # automóvel que faz 12 Km por litro.
    litros_usados = distancia / 12
    return litros_usados


def mostrar_resultado(tempo_gasto, velocidade_media, distancia, litros_usados):
    print('#' * 20)
    print(f'Velocidade Média: {velocidade_media}')
    print(f'Tempo Gasto Na Viagem: {tempo_gasto}')
    print(f'Distância Pecorrida: {distancia}')
    print(f'Litros Usados Na Viagem: {round(litros_usados, 2)}')
    print('#' * 20)

tempo_gasto, velocidade_media = ler_valores()
distancia = calcular_distancia(tempo_gasto, velocidade_media)
litros_usados = calcular_litros(distancia)
mostrar_resultado(tempo_gasto, velocidade_media, distancia, litros_usados)