def recursao(i):
    if i == 5:
        return
    i += 1

    print('Recursao')
    return recursao(i)

recursao(0)
