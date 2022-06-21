#Polimorfismo

class Arma:

    def __init__(self, balas, peso):
        self.balas = balas
        self.peso = peso #Kg

    def disparar(self):
        print("El arma dispara");

class Pistola(Arma):

    def disparar(self):
        return super().disparar()


arma = Arma(15,7)
arma.disparar()
pistola = Pistola(12, 5)
pistola.disparar()
