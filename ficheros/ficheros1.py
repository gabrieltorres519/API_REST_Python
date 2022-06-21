# file = open('file.txt','r');

# dato = file.read()

# file.close();

# print(dato);

def leer_fichero():
    file = open('/home/gabriel/Documentos/PythonIntroduccion/ficheros/file.txt', 'r')

    dato = file.read()

    file.close()

    print(dato)


def escribir_fichero():
    file = open('/home/gabriel/Documentos/PythonIntroduccion/ficheros', 'w')

    dato = "Mi apellido es Fenske"

    file.write(dato)

    file.close()


def escribir_sin_borrar():
   file = open('/home/gabriel/Documentos/PythonIntroduccion/ficheros', 'a')
   dato = "\nEsta linea es nueva y la estoy agregando sin borrar nada"
   file.write(dato)
   file.close()


leer_fichero()
