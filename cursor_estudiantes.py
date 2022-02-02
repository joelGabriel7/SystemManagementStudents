from conexion_estudiantes import ConexionEstudiantes
from logger_base import log

class CursorPoolEstudiantes:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inciamos el metodo with __enter__')
        self._conexion = ConexionEstudiantes.creando_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.debug(f'Ocurrio un error: {tipo_excepcion}, {valor_excepcion}, {detalle_excepcion}')

        else:
            self._conexion.commit()
            log.debug('Se hizo commit de la transaccion')
        self._cursor.close()
        ConexionEstudiantes.LiberarConexion(self._conexion)
if __name__ == '__main__':
    with CursorPoolEstudiantes() as cursor:
        print('Abriendo el cursor con with')
        cursor.execute('SELECT * FROM estudiantes_universitarios ORDER BY id_estudiante')
        print(cursor.fetchall())
