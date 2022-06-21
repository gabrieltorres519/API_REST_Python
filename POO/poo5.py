#Polimorfismo

class Arma:

    def __init__(self, balas, peso):
        self.balas = balas
        self.peso = peso #Kg

    def disparar(self):
        print("El arma dispara");

class Pistola(Arma):

    # El polimorfismo se aplica cuando el mismo método de la clase padre hace algo diferente en la clase hija
    def disparar(self):
        print("El arma dispara lento");

class Ametralladora(Arma):

    def disparar(self):
        print("El arma dispara rápido");



arma = Arma(15,7)
arma.disparar()

pistola = Pistola(12, 5)
pistola.disparar()

ametralladora = Ametralladora(50, 12)
ametralladora.disparar()

