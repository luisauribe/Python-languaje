mi_diccionario = {"One" : "Uno", "Two" : "Dos", "Three" : 3, 4 : "Cuatro"}
print(mi_diccionario)

# Agregar más elementos a un diccionario y cambiar el valor de una clave
mi_diccionario["Five"] = "Seis"
print(mi_diccionario)
mi_diccionario["Five"] = "Cinco"
print(mi_diccionario)

# Eliminar un elemento
del mi_diccionario["Two"]
print(mi_diccionario)

# Utilizar una tupla para asignar las claves a cada uno de los valores
mi_tupla = ('Blue', 'Yellow', 'Green', 'Black')
mi_diccionario_2 = {mi_tupla[0] : "Azul", mi_tupla[1] : "Amarillo", mi_tupla[2] : "Verde", mi_tupla[3] : "Negro"}
print(mi_diccionario_2)

# Almacenar en un diccionario una tupla.
mi_diccionario_3 = {"Juan" : 20, "Paula" : 20, "Tomas": 18, "Luisa" : 17, "Nacimiento" : (2000, 2000, 2002, 2003)}
print(mi_diccionario_3)
print(mi_diccionario_3["Nacimiento"][2:])
print(mi_diccionario_3["Juan"])
print(mi_diccionario_3["Luisa"])


# Almacenar un diccionario dentro de otro diccionario
mi_diccionario_4 = {"Isaac" : 16, "Sara" : 16, "Simon": 14, "Camila" : 12, "Años" : {"Nacimiento" : (2004, 2004, 2006, 2008)}}
print(mi_diccionario_4)
print(mi_diccionario_4["Años"]["Nacimiento"][0])
print(mi_diccionario_4["Isaac"])
print(mi_diccionario_4["Sara"])
print(mi_diccionario_4["Años"]["Nacimiento"][3])
print(mi_diccionario_4["Camila"])

# Imprimir las claves de un diccionario con el metodo "keys"
print(mi_diccionario_4.keys())
# Imprimir los valores de un diccionario con el metodo "values"
print(mi_diccionario_4.values())

# Imprimir la longitud de un diccionario
print(len(mi_diccionario))
print(len(mi_diccionario_2))
print(len(mi_diccionario_3))
print(len(mi_diccionario_4))

# Unir dos diccionarios
mi_diccionario.update(mi_diccionario_2)
print(mi_diccionario)
