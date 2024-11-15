"""
  *Metacaracteres*
 . - Qualquer Caractere (execeto linha nova)
 \w - Qualquer Caractere Alfanumerico
 \W - Qualquer Caractere NÃ0-Alfanumerico
 \d - Qualquer Caractere que seja um digito (0-9)
 \D - Qualquer Caractere que NÃO seja um digito (0-9)
 \s - espaço em branco
 ^ - Começa com a letra passada
 $ - Termina com a letra passada

 '\' - usado antes de qualquer Metacaracteres para espesificar o sentido literal

  *Quantificadores*
  '[]' - Padrão Opicional
  '()' - Captura Grupos da Caracteres
  '*' - de zero a mais vezes (carectes | digitos)
  '?' - zero ou uma vez (carectes | digitos)
  '+' - uma ou mais vezes (carectes | digitos)
  {m,n}  - de 'm a 'n' vezes
  '|' ou
"""
import re

# Função Search
frase = 'Olá, meu número de telefone é (42)00010-0000'
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)) # Encontrar um numero de telefone REGEX

frase_car = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
print(re.search('[A-Za-z]{3}-\d{4}', frase_car))

email = 'Entre em contato, meu email é teste@teste.com'
print(re.search('\w+@+\w+\.\w+',email)) # Encontrar um email

# Função match (Encontra  somente no inicio da String)
frase_placa = 'A placa de carro que eu anotei durante a batida foi FRT-1998'
frase_placa_2 = 'FRT-1998 é a placa do carro'
print(re.match('[A-Za-z]{3}-\d{4}', frase_placa))
print(re.match('[A-Za-z]{3}-\d{4}', frase_placa_2))

# find_all
frase3 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3))

emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''
print(re.findall('\w+@+\w+\.\w*',emails))
