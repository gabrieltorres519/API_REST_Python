# Encapsulamiento (no existe en el lenguaje pero se simula de la manera siguiente)

class Curso:

    __titulo = "Backend Python3"
    __duracion = 20

    def __adquirir_curso(self):
        print("Has adquirido este curso");

    # Simulando setters y getters para trabajar con atributos y metodos privados (encapsulados)
    def get_adquirir_curso(self):
        return self.__adquirir_curso();
    


curso = Curso()
# curso.__titulo # No se podrá acceder porque es privado
# curso.__duracion # No se podrá acceder porque es privado
# curso.__adquirir_curso() # No se podrá acceder porque es privado

curso.get_adquirir_curso();