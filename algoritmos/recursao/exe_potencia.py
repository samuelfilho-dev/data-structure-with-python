def potencia(b, a):
    if a < 0:
        return 0

    if a == 0 or a == 1:
        return b

    return b * potencia(b, a - 1)


print(potencia(2, 2))
