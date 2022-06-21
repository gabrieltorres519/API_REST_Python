from lib2to3.pytree import convert


class Usuario:

    def __init__(self, nombre, apellido, edad, persona_masculina):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.persona_masculina = persona_masculina
        self.premium = False

    def __repr__(self):
        return f"{self.nombre}, {self.apellido}, {self.edad}, {self.persona_masculina}, {self.premium}"

    def convertir_premium(self):
        self.premium = True;


usuario = Usuario("Gaston", "Torres", 22, True);
print(usuario);
print(usuario.premium);
usuario.convertir_premium();
print(usuario);
print(usuario.premium);



