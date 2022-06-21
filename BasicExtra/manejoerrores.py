try:
    menu = int(input("Ingrese un numero entero: "));
    print(f"Ha ingresado la opcion {menu}");
except ValueError as error:
    print(f"No puede ingresar ese tipo de dato, el error es: {error}");