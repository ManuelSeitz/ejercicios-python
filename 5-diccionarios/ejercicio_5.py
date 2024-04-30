"""Construye un sistema escolar entero para BigBayData.com.
Para ello, el diccionario principal contendrá los cursos con la información de precio y nombre.
Dentro de estas, existirán nuevos diccionarios para almacenar la siguiente información: 
'profesor, contacto, lista de alumnos totales, evaluación promedio'."""

CURSOS = [
    {
        "nombre": "Programación",
        "precio": 250.00,
        "info": {
            "profesor": "",
            "contacto": "",
            "lista-alumnos": [],
            "evaluacion-promedio": 0
        }
    }
]

while True:
    print('CURSOS')
    print("""
        1.Agregar curso
        2.Consultar curso
        0.Salir
    """)
    OPERACION = 0

    try:
        OPERACION = int(input('Ingresa la operación que desea realizar: '))
    except ValueError:
        print('Ingresaste un valor incorrecto.')
        continue

    if OPERACION == 0:
        break

    if OPERACION == 1:
        while True:
            print('NOMBRE DEL CURSO')
            NOMBRE = input('Ingresa el nombre del curso: ')

            print('PRECIO')
            PRECIO = 0
            VALOR_CORRECTO = False
            while not VALOR_CORRECTO:
                try:
                    PRECIO = float(input('Ingresa el precio del curso: '))
                    VALOR_CORRECTO = True
                except ValueError:
                    print('Valor incorrecto.')

            print('PROFESOR')
            NOMBRE_PROFESOR = input('Ingresa el nombre del profesor: ')

            print('CONTACTO')
            CORREO_PROFESOR = input('Ingresa el correo del profesor: ')

            print('LISTA DE ALUMNOS')
            STRING_ALUMNOS = input(
                'Ingresa los alumnos del curso separados por una coma: ')
            LISTA_ALUMNOS = STRING_ALUMNOS.split(',')
            for alumno in LISTA_ALUMNOS:
                # Eliminar los espacios en blanco antes y después del nombre
                alumno = alumno.strip()

            print('EVALUACIÓN PROMEDIO')
            VALOR_CORRECTO = False
            while not VALOR_CORRECTO:
                try:
                    EVALUACION_PROMEDIO = float(
                        input('Ingresa la evaluación promedio: '))
                    VALOR_CORRECTO = True
                except ValueError:
                    print('Valor incorrecto.')

            TEMPLATE_CURSO = {
                "nombre": NOMBRE,
                "precio": PRECIO,
                "info": {
                    "profesor": {"nombre": NOMBRE_PROFESOR, "correo": CORREO_PROFESOR},
                    "contacto": CORREO_PROFESOR,
                    "lista-alumnos": LISTA_ALUMNOS,
                    "evaluacion-promedio": EVALUACION_PROMEDIO
                }
            }

            CURSOS.append(TEMPLATE_CURSO)
            print('Curso cargado con éxito.')

            CONTINUAR = False
            while True:
                try:
                    CONTINUAR = bool(
                        int(input('¿Desea ingresar otro curso? 1 para SÍ, 0 para NO: ')))
                    break
                except ValueError:
                    print('Valor incorrecto.')

            if not CONTINUAR:
                break

    elif OPERACION == 2:
        while True:
            print('CONSULTA')
            NOMBRE_CURSO = input('Ingresa el nombre del curso a consultar: ')
            CURSO_ENCONTRADO = False
            for curso in CURSOS:
                if curso["nombre"].lower() == NOMBRE_CURSO.lower():
                    CURSO_ENCONTRADO = True
                    print(curso)
                    break
            if not CURSO_ENCONTRADO:
                print('No se encontró el curso.')
                continue
            input('Pulse ENTER para salir.')
            break
    else:
        print('Operación inválida.')
