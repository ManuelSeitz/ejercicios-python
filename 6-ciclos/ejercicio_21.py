"""Un centro educativo nos ha pedido que diseñemos una aplicación para calcular algunos datos
estadísticos de las edades de los alumnos. Se ingresarán datos hasta que uno de ellos sea negativo.
La aplicación mostrará la suma de todas las edades, 
cuantos alumnos ingresamos y cuantos son mayores."""

cantidad_alumnos = 0
suma_edades = 0
mayores_de_edad = 0
while True:
    edad_alumno = int(input('Ingrese la edad del alumno: '))
    if edad_alumno < 0:
        break
    suma_edades += edad_alumno
    cantidad_alumnos += 1
    if edad_alumno >= 18:
        mayores_de_edad += 1

print('Cantidad de alumnos:', cantidad_alumnos)
print('Suma de edades:', suma_edades)
print('Alumnos mayores de edad:', mayores_de_edad)
