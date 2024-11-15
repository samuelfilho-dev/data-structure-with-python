import re
texto = "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e 11111-111 meu site é https://www.iaexpert.academy http://iaexpert.com.br"

print(re.findall('\d', texto))
print(re.findall('[0-9]{5}-[0-9]{3}', texto))
print(re.findall('https?://[A-za-z0-9./]+',texto)) # Encontrar Link