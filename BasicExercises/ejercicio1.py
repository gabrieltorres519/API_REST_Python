"""Crear un programa que le pida al usuario su nombre, su edad,
y luego lo salude y asu edad le reste 5 años
-Recorda crear las dos variables {nombre} y {edad} y a cada una de ellas
asignarle la funcion input para que el usuario pueda ingresar los datos y
espisifcando siempre que tipo de dato va a ser cada varible (str, int, float, bool)
-Despues con un print y concatentando mensajes y variables mostrar el resultado
final"""

nombreIngresado = str(input("Ingrese su nombre: "));
edadIngresada = int(input("Ingrese su edad: "));

print(f"Hola {nombreIngresado}!, tu edad es de {edadIngresada} años!!, que restandole 5 es {edadIngresada - 5}");