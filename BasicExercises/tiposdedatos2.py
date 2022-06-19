# Listas

from time import process_time_ns


nombres = ["Gaston", "Belen", "Juan", "Marta"];
edades = [12,90,72,48];
numeros = [1900, 20022];
# apellidos = [["Torres", "Mendoza"], ["Perez", "Rodriguez"], ["Gonzales", "Vilches"]];
apellidos = [
    ["Torres", "Mendoza"], 
    ["Perez", "Rodriguez"], 
    ["Gonzales", "Vilches"], 
    25, 
    "Holaaa"
];

"""
print(nombres);
nombres.append("Marcelo");
print(nombres);
nombres.pop();
print(nombres);
cantidad_elementos = len(nombres)
print(cantidad_elementos)
print(nombres[-1])
print(nombres[0:2])
"""

"""

print(apellidos[0]);
print(apellidos[0][0]);

"""


print(max(edades))
print(min(edades))
print(sorted(edades))

edades.remove(72)
print(edades)

edades.reverse()
print(edades)

edades.extend(numeros)
print(edades)


for nombre in nombres:
    print(nombre)


pares = []
for i in range(10):
    if i % 2 == 0:

        pares.append(i)
print(pares) 


pares2 = [i for i in range(100) if i % 2 == 0];
print(pares2)





