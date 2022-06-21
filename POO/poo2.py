from lib2to3.pytree import convert


class Usuario:

    """
     Atributos de la clase en sí
    """
    cantidad_usuarios = 100; 

    """
     Atributos que tendrán los objetos que se instancien de la clase
    """
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

    def mirar_peliculas(self):
        if self.premium:
            print("El usuario puede mirar las películas");
        else:
            print("El usuario no es premium");

    
    """
     Los métodos estáticos son accesibles sin la necesidad de instanciar un objeto de la clase,
     para esto utilizamos un decorador de Python que ya viene por defecto con el lenguaje (no 
     tenemos que crearlo) llamado @staticmethod
    """

    @staticmethod
    def usuario_mayor(edad):
        return edad >= 18;

    @classmethod
    def mi_cantidad_usuarios(cls):
        return cls.cantidad_usuarios;




usuario = Usuario("Gaston", "Torres", 22, True);

print(usuario);
print(usuario.premium);
usuario.mirar_peliculas()
usuario.convertir_premium();
print(usuario);
print(usuario.premium);
usuario.mirar_peliculas()


es_mayor = Usuario.usuario_mayor(18);
print(es_mayor);

cantidad_usuarios = Usuario.mi_cantidad_usuarios();
print(cantidad_usuarios);
