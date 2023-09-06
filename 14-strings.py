text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')

'''
#Cantidad de caracteres
size = len(text)
print(size)

print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))

# Hacer que comience con minuscula
print(text.swapcase())
# Si el texto incia con:
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
#Para poner primer caracter en mayúscula
print(text_2.capitalize())
#Para poner cada primera letra de cada palabra del texto en mayúscula
print(text_2.title())
#Si descubre si es o no un digito (incluso si es un string)
print(text_2.isdigit())
print("398".isdigit())