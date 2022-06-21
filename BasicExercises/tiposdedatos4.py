# Tuplas => Listas(arrays) que no puedes modificar

tupla = (100, "hi", ["familia","amigos"],{"hello":"Hola!"})

print(tupla)
print(tupla[0])
print(tupla[-1])

# No se puede modificar, da error
#tupla[0] = 200;

# No se pueden agregar elementos, solo que se convierta en lista
tupla = list(tupla);
tupla.append(200)
tupla = tuple(tupla);

print(tupla);

