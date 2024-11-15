def ler_graus_celus():
    graus_celsus = float(input('Temperatura em celsius(ºC): '))
    return graus_celsus

def converter_celsus_fahrenheit(graus_celsus):
    graus_fahrenheit = (9 * graus_celsus + 160) / 5
    return graus_fahrenheit

def print_resultado(fahrenheit_temp):
    print(f'A Temperatura em Fahrenheit (ºF): {fahrenheit_temp:.2f}')


celsus = ler_graus_celus()
fahrenheit = converter_celsus_fahrenheit(celsus)
print_resultado(fahrenheit)
