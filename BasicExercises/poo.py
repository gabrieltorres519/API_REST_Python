class Auto:

    def __init__(self, marca, color, cantidad_ruedas, velocidad_maxima):
        self.marca = marca
        self.color = color
        self.cantidad_ruedas = cantidad_ruedas
        self.velocidad = velocidad_maxima
        self.motor = 2.0



aventador = Auto("Lamborgini","blanco",4,320)

print(aventador) # Se imprime la dirección en memoria en la que se está almacenando el objeto Auto Aventador
