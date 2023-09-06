text = "Ella sabe Python"
print(text[0])
print(text[1])
# print(text[999])
size = len(text)
print('size => ',size)
print(text[size - 1])
print(text[-1])

# slicing

print(text[0:5])
print(text[10:16])
#Parte de 0
print(text[:10])
#Hasta el final sin el último caracter
print(text[5:-1])
#Hasta el final totalmente
print(text[5:])
#De inicio a fin
print(text[:])
#Inicio a Fin con saltos
print(text[10:16:1])
print(text[10:16:2])
#De inicio a Fin con saltos
print(text[::2])