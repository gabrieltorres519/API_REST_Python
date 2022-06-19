def saludar():
    print("Hola!!");
    return "Hola!!"

def despedida():
    print("Adios...");
    return "Adios..."

def sumar(a,b):
    print(f"La suma es: {a+b} \n");
    return a+b

def main():
    option = int(input("""

    Inserte el número de función que desee utilizar:
    [1] Funcion saludar.
    [2] Funcion despedida.
    [3] Funcion sumar.
    [4] Salir

    >>> """));


    if option == 1:
        saludar();
    elif option == 2:
        despedida();
    elif option == 3:
        a = int(input("Ingrese el primer número a sumar: "));
        b = int(input("Ingrese el segundo número a sumar: "));

        sumar(a,b);
    elif option == 4:
        print("Cerrando el programa...");
        exit();
    else:
        print("La opción no existe!! ");
        exit();


while True:
    main();
    
