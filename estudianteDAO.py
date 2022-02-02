from estudiante import Estudiantes
from cursor_estudiantes import CursorPoolEstudiantes


class EstudiantesDao:
    _SELECT = 'SELECT * FROM estudiantes_universitarios ORDER BY id_estudiante'
    _BUSCADOR = 'SELECT * FROM estudiantes_universitarios WHERE matricula= %s'
    _INSERTAR = 'INSERT INTO estudiantes_universitarios (matricula,nombre,apellido,carrera,edad)VALUES(%s, %s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE estudiantes_universitarios SET nombre=%s,apellido=%s, carrera=%s, edad=%s WHERE matricula=%s'
    _DELETE = 'DELETE FROM estudiantes_universitarios WHERE matricula=%s'

    @classmethod
    def MostrarEstudiantes(cls):
        with CursorPoolEstudiantes() as cursor:
            cursor.execute(cls._SELECT)
            students = cursor.fetchall()
            studentes = []
            for student in students:
                estu = Estudiantes(student[0], student[1], student[2], student[3], student[4], student[5])
                studentes.append(estu)
            return studentes

    @classmethod
    def RegisterStudents(cls, estudiante):
        with CursorPoolEstudiantes() as cursor:
            valores = (estudiante.matricula, estudiante.nombre, estudiante.apellido,
                estudiante.carrera,
                estudiante.edad)
            cursor.execute(cls._INSERTAR, valores)
            print(f'Registered Students: {estudiante}'.center(50, '='))
            return cursor.rowcount

    @classmethod
    def BuscadorEstudiantes(cls, estudiante):
        with CursorPoolEstudiantes() as cursor:
            valor = (estudiante,)
            cursor.execute(cls._BUSCADOR, valor)
            mat = cursor.fetchall()
            matri = []
            for student in mat:
                estu = Estudiantes(student[0], student[1], student[2], student[3], student[4], student[5])
                matri.append(estu)
            return matri

    @classmethod
    def ActualizarEstudiante(cls, students):
        with CursorPoolEstudiantes() as cursor:
            valores = (students.nombre, students.apellido, students.carrera, students.edad, students.matricula)
            cursor.execute(cls._ACTUALIZAR, valores)
            print('Students Updated'.center(50, '='))
            return cursor.rowcount

    @classmethod
    def EliminarEstudiantes(cls, student):
        with CursorPoolEstudiantes() as cursor:
            valores = (student.matricula,)
            cursor.execute(cls._DELETE, valores)
            print(f'Studentes Delete'.center(50, '='))
            return cursor.rowcount

if __name__ == '__main__':
    # estudiantes = EstudiantesDao.MostrarEstudiantes()
    # print('Show Students'.center(50, '='))
    # for x in estudiantes:
    #     print(x)


    # estudiantes1= Estudiantes(nombre='Mario', apellido='Ortiz', carrera='lic.Administracion de empresas', edad=20, matricula='1215078',id_estudiante=5)
    # EstudiantesDao.ActualizarEstudiante(estudiantes1)
    # print(f'Students Updated: {estudiantes1}')


    studen = Estudiantes(matricula=1216547, nombre='Marta', apellido='Fernadez', carrera='lic.Administracion de empresas', edad=19,)
    EstudiantesDao.RegisterStudents(studen)
    print(f'Students registered: {studen}')
    #
    # studiant = Estudiantes(matricula='1217488')
    # EstudiantesDao.EliminarEstudiantes(studiant)
    # print(f'Student Deleted:{studiant}')

    # print('Searched Students'.center(50, '='))
    # search = EstudiantesDao.BuscadorEstudiantes('1215078')
    # for s in search:
    #     print(s)
