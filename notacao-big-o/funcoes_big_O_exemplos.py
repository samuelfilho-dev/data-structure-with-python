lista = [1, 2, 3, 4, 5]


def constant(n):
    print(n[0])


constant(lista)


def linear(n):
    for i in n:
        print(i)


linear(lista)


def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('-----')


quadratic(lista)


# O(1) + O(5) + O(n) + O(N) + O(3)
# O (9) + O(2n) -> O(n)
def combination(n):
    # O (1)
    print(n[0])

    # O (1)
    for i in range(5):
        print('teste', i)

    # O (N)
    for i in n:
        print(i)

    # O (N)
    for i in n:
        print(i)

    # 0 (3)
    print('Python')
    print('Python')
    print('Python')
    print('Python')


combination(lista)
