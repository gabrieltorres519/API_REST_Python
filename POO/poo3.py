#Pasando objeto como parámetro a otro objeto
class Catalogo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []

class Pelicula:

    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion #minutos
        self.genero = genero

    ## Nos sirve cuando queremos poder usar el método dentro de otra clase que no sea esta misma
    ## como al pasar por parámetros un objeto de esta clase a otra clase
    def __repr__(self):
        return f"{self.nombre}, {self.duracion}, {self.genero}"

catalogo1 = Catalogo("Catalogo de terror");
pelicula = Pelicula("Actividad paranormal", 120, "terror");

print(catalogo1.peliculas);
catalogo1.peliculas.append(pelicula);
print(catalogo1.peliculas); #Es una lista (array)
print(catalogo1.peliculas[0]); #El elemento es accesible en la lista como un array 
print(catalogo1.peliculas[0].nombre); # Cada elemento de esa lista será un objeto de la clase Pelicula 



