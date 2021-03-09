print("Evalua tu nota")
# Funcion que recibe el valor para una variable a través del teclado (input())
nota_alumno = input("Introduce tu nota: ")

# Evalua la nota de un alumno
def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Suspendido"
    return valoracion

# El valor numerico que el usuario introduzca se almacenara en la variable "nota"
print(evaluacion(float(nota_alumno)))
