# Pograma que comprueba la edad de un usuario
print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad: "))

if edad_usuario < 18:
    print("Denegado")
elif edad_usuario > 100:
    print("Este numero no es correcto")
else:
    print("Bienvenido")

# Programa que evalua si la nota de un alumno es suficiente para pasar
print("Evalua tu nota")

nota_alumno = float(input("Introduce una nota del 0 al 5: "))

if nota_alumno <= 3.4:
    print("Reprobado.")

elif nota_alumno == 3.5:
    print("Uyyy, raspando, trata de mejorar.")

elif nota_alumno == 4.5:
    print("Bien hecho!!! :)")

elif nota_alumno == 4.8:
    print("Muy bien!!!")

elif nota_alumno == 4.9:
    print("Excelente!!!")

elif nota_alumno > 5:
    print("ups, este número no es correcto. :(")

else:
    print("Felicitaciones, sobresaliste!!!")
