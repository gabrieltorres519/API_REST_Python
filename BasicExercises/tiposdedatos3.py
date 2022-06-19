# Diccionarios

palabras_ingles = {
    "hello":"hola",
    "day":"dia",
    "mess":"desorden"
}

print(palabras_ingles)
print(palabras_ingles["hello"]);


palabras_ingles["hello"] = "salut"
print(palabras_ingles)
print(palabras_ingles["hello"])

# Sin usar clave y valor
for palabra in palabras_ingles:
    print(f"{palabra} : {palabras_ingles[palabra]}");

# Usando clave y valor 
for clave, valor in palabras_ingles.items():
    print(clave, valor)


alumnos = [
    {
        "nombre": "Gabriel",
        "apellido": "Torres",
        "edad": 22
    },
        {
        "nombre": "Marcelo",
        "apellido": "Paniagua",
        "edad": 24
    },
        {
        "nombre": "Mariel",
        "apellido": "López",
        "edad": 45
    },
        {
        "nombre": "Emmanuel",
        "apellido": "Sirangua",
        "edad": 19
    }
]


print(alumnos);

print("\n");

print(alumnos[0]);

print("\n");

print(alumnos[0]["nombre"]);
