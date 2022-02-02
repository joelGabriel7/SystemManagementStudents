from estudianteDAO import EstudiantesDao
from estudiante import Estudiantes

op = None
while op != 6:
    print('Welcome to System Managemente Students'.center(50, '='))
    print()
    print('1.Show students')
    print('2.Add students')
    print('3.Search students')
    print('4.Update students')
    print('5.Delete students')
    print('6.Exit')
    op = int(input('Write the one options: '))

    if op == 1:
        estudiantes = EstudiantesDao.MostrarEstudiantes()
        print('Shows Students'.center(50, '='))
        for x in estudiantes:
            print(x)

    elif op == 2:


        matri = input('Enter the enrollment(matricula): ')
        nom = input('enter your name: '.capitalize())
        ape = input('Enter your last name: '.capitalize())
        carre = input('Enter the carrer of students: '.capitalize())
        edad = int(input('Enter the age of student: '))

        eje = Estudiantes(matricula=matri, nombre=nom.capitalize(), apellido=ape.capitalize(), carrera=carre.capitalize(), edad=edad)
        EstudiantesDao.RegisterStudents(eje)
        print(f'Registered Students: {eje}')

    elif op == 3:
        searchs = str(input('Enter the enrollment of students: '))
        search = EstudiantesDao.BuscadorEstudiantes(searchs)
        s=''
        for s in search:
            print(f'student found: {s}')
        if s not in search:
            print('Student not has been found..!!')





    elif op == 4:
        m_udpte = input('Enter the enrollment(matricula): ')
        nom_update = input('Enter your name: ')
        ape_update = input('Enter your last name: ')
        carre_update = input('Enter the carrer of students: ')
        edad_update = int(input('Enter the age of student: '))
        studen = Estudiantes(nombre=nom_update.capitalize(), apellido=ape_update.capitalize(), carrera=carre_update.capitalize(), edad=edad_update,
                             matricula=m_udpte)
        EstudiantesDao.ActualizarEstudiante(studen)
        print(f'Students updated : {studen}')

    elif op == 5:
        m_delete = input('Enter the enrollment(matricula): ')
        studiant = Estudiantes(matricula=m_delete)
        EstudiantesDao.EliminarEstudiantes(studiant)
        print(f'this student has been eliminated:{studiant}'.capitalize())

    elif op == 6:
        print('We exit the system...!!'.center(50,'='))
        break
    else:
        print('Please enter one option of menu..!!!')
        continue
