class Auto:

    def __init__(self, marca, color, cantidad_ruedas, velocidad_maxima):
        self.marca = marca
        self.color = color
        self.cantidad_ruedas = cantidad_ruedas
        self.velocidad = velocidad_maxima
        self.motor = 2.0
        self.motores = [2.1,2.5,4.2,2.2]
        self.marcas_preestablecidas = {"altagama": "audi", "bajagama": "toyota"}

    """
      El método string será ejecutado siempre que se llame al objeto instanciado, aún cuando solo se llame a alguno
      de sus atributos.
    """
    def __str__(self):
        return f"Auto: {self.motor}, {self.color}, {self.marca}, {self.cantidad_ruedas}, {self.velocidad} \n";

    """
     Métodos propios
    """
    def acelerar(self):
        print(f"El auto ha acelerado hasta {self.velocidad} km/hr");

    def frenar(self):
        print(f"El auto va a frenar");



aventador = Auto("Lamborgini","blanco",4,320);
huracan = Auto("Lamborgini", "rojo", 4, 300);

print(aventador); # Se imprime la dirección en memoria en la que se está almacenando el objeto Auto Aventador
                  # Después de agregar el método __str__ ya no se imprime la dirección en memoria, sino solo __str__
#print(aventador.motor); # Se imprimirá dos veces el motor si tenemos el Método __str__ sin comentar
print(huracan);


aventador.acelerar();
aventador.frenar();
huracan.acelerar();
huracan.frenar();


aventador.color = "amarillo";
print(aventador);


print(aventador.motores[1]);
print(aventador.marcas_preestablecidas["altagama"]);
 