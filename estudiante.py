class Estudiantes:
    def __init__(self, id_estudiante=None, matricula=None, nombre=None, apellido=None, carrera=None, edad=None):
        self._id_estudiante = id_estudiante
        self._matricula = matricula
        self._nombre = nombre
        self._apellido = apellido
        self._carrera = carrera
        self._edad = edad

    def __str__(self):
        return f"""
                Id: {self._id_estudiante}, Matricula: {self._matricula}, Nombre: {self._nombre},
                Apellido: {self._apellido} , Carrera: {self._carrera}, Edad: {self._edad}
                 """

    @property
    def id_estudiante(self):
        return self._id_estudiante

    @id_estudiante.setter
    def id_estudiante(self, id_estudiante):
        self._id_estudiante = id_estudiante

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


if __name__ == '__main__':
    pass
