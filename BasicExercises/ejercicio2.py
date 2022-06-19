"""
Hacer un programa que le pida al usuario que ingrese su edad y su sexo,
si el usuario es mayor de edad y ademas es menor de 65 años le debe permitir
al usuario quedarse en el programa, en caso
contrario el programa debe deternese. Si es sexo es masculino que el programa
salude al usuario como un caballero y si el sexo es femino que el programa salude al
usuario como una dama
-Para que el usuario ingrese su sexo hacer un menu con condiciones.
"""

from glob import escape


edad = int(input("Ingrese su edad: "));
sexo = int(input("""
    Ingrese su sexo:
    [1] Masculino
    [2] Femenino
 >> """));

if sexo == 1:
    persona_masculina = True;
elif sexo == 2:
    persona_masculina = False;
else:
    print('Dato no contemplado');
    exit();

if edad < 65 and edad > 18:
    print("Se ha permitido que permanezcas en el programa");
    if persona_masculina == True:
        print(f"Hola Caballero, su edad es de {edad} años\n");
    else:
        print(f"Hola Dama, su edad es de {edad} años \n");
else:
    print("No entras en el rango de edad, saliendo del programa...");
    exit();