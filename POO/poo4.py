class Animal:

    def __init__(self, edad, numero_patas, alimentacion):
        self.edad = edad
        self.numero_patas = numero_patas
        self.alimentacion = alimentacion
    
    def caminar(self):
        print("El animal camina");
    
    def correr(self):
        print("El animal corre");

# La clase padre va entre paréntesis
class Perro(Animal):
    
    raza = None
    ladrido = None
    pelaje = None

    def ladrar(self):
        print("El perro ladra");

    def morder(self):
        print("El perro muerde");

    

perro = Perro(3, 4, "Carnivoro");
perro.raza = "Caniche"
perro.ladrido = "Fuerte"
perro.pelaje = "Blanco"

print(perro.edad)
print(perro.numero_patas)
print(perro.alimentacion)
print(perro.raza)
print(perro.ladrido)
print(perro.pelaje)





        
