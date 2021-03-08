mi_tupla = ("Nombres", "laura", "Daniela","Numeros", 1, 2, 3.14)
print(mi_tupla[:])

# Para convertir una tupla en una lista con el metodo "list"
mi_lista = list(mi_tupla)
#La variable "mi_lista" almacena una lista que se ha creado a partir de una tupla
print(mi_lista)


# Para convertir una lista en tupla con el metodo "tuple"
mi_lista_2 = ["Juan", 20, "Tomas", 18, "Isaac", 16, 20]
print(mi_lista_2[:])
mi_tupla_2 = tuple(mi_lista_2)
#La variable "mi_tupla_2" almacena una tupla que se ha creado a partir de una lista
print(mi_tupla_2)


# Comprobar si hay un elemento dentro de una tupla con el metodo "in"
print("Juan" in mi_tupla_2)

# Comprobar cuantos elementos se encuentran en una tupla con "count"
print(mi_tupla_2.count(20))

# Averiguar la longitud de una tupla con el metodo "len"
print(len(mi_tupla_2))

# Tuplas unitarias: tuplas con un unico elemento
tupla_1 = ('a',)
print(tupla_1)

# Asignar valores de una tupla a nuevas variables
nombre, edad, nombre_2, edad_2, nombre_3, edad_3, numero = mi_tupla_2
print(nombre, edad)
print(nombre_2, edad_2)
print (nombre_3, edad_3)
print(numero)
