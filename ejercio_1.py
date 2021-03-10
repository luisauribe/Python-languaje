num_1 = int(input("Introduce un numero: "))
num_2 = int(input("Introduce otro numero: "))

def devuelve_max(num_1, num_2):
    if num_1 > num_2:
        print("El número más alto es: ", num_1)
    elif num_1 < num_2:
        print("El número mas alto es: ", num_2)
    else:
        print("Son iguales")

devuelve_max(num_1, num_2)
