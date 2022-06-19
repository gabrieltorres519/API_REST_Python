from click import prompt


nombre = "Francisco"
edad = 21
persona_masculina = True

edadIngresada = int(input("Ingresa tu edad: "));

if edadIngresada > 21 and edadIngresada < 25:
    print("Eres menor de 25 pero eres mayor de edad!!");
elif edadIngresada < 25:
    print("Hola eres menor de 25");


if nombre == "Gaston":
    print("Hola Gaston");
elif nombre == "Frida":
    print("Hola Frida");
else:
    print("Tu nombre no está contemplado");
    if nombre == "":
        print("El nombre es vacio")


if persona_masculina:
    print("Persona masculina");