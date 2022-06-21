class Auto:

    def __init__(self, marca, color, cantidad_ruedas, velocidad_maxima):
        self.marca = marca
        self.color = color
        self.cantidad_ruedas = cantidad_ruedas
        self.velocidad = velocidad_maxima
        self.motor = 2.0

    """
      El método string será ejecutado siempre que se llame al objeto instanciado, aún cuando solo se llame a alguno
      de sus atributos.
    """
    def __str__(self):
        return f"{self.motor}";

aventador = Auto("Lamborgini","blanco",4,320);

print(aventador); # Se imprime la dirección en memoria en la que se está almacenando el objeto Auto Aventador
print(aventador.motor); # Se imprimirá dos veces el motor si tenemos el Método __str__ sin comentar

