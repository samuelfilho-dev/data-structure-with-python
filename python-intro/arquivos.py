with open('arquivos/frase1.txt') as tex: # Ler um arquivo
    for linha in tex:
        print(linha)

with open('arquivos/frase1.txt') as tex: # Guardar as Frases em uma lista
    r = tex.readlines()

print(r)

with open('arquivos/texto2.txt', 'w') as texto: # Criar um arquivo
    texto.write('Olá Mundo')