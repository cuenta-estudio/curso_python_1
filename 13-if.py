if True:
  print('deberá ejecutarse')

if False:
  print('nunca se ejecuta')

'''
pet = input('¿Cuál es tu mascota favorita? ')

if pet == 'perro':
  print('genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo maximo')
else:
  print('no tienes ninguna mascota interesante')


stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')

'''

number = int(input('Ingrese un numero => '))
result = number % 2
if (result == 0):
	print('Es par')
else:
	print('Es impar')
     
# Si es par o impar pero a través de un String

number = '10'
print(number)

# Escribe tu solución 👇
number2 = int(number) % 2

if number2 == 0:
  print("Es par")
else:
  print("Es impar")