mi_lista = [17, 39, "Laura", True]
print(mi_lista)

# Asigna un valor nuevo al indive 1
mi_lista[1] = 7
print(mi_lista[:])

# Accede al indice 1 e imprime desde el 1 hasta el 3 omitiendo el 3
print(mi_lista[1:3])

# Imprime la lista completa
print(mi_lista[:])

# Agrega un nuevo elemento al final de la lista
mi_lista.append("Maria")
print(mi_lista[:])

# Empieza a contar desde el final de la lista
print(mi_lista[-2])

# Accede al indice e imprime los dos últimos elementos hastael final de la lista
print(mi_lista[2:])

# Añade un elemento en el indice deseado
mi_lista.insert(3,50.87)
print(mi_lista[:])

# Toma una lista como argumento y agrega todos los elementos
lista_2 = ["Numeros", 5, 87.32]
mi_lista.extend(lista_2)
print(mi_lista[:])

# Muestra el indice en el que se encuentra un element
print(mi_lista.index("Maria"))

# Revisa si hay dicho elemento en la lista
print("Laura" in mi_lista)

# Elimina elementos de la lista
mi_lista.remove(True)
print(mi_lista[:])

# Elimina el ultimo elemento de la lista
mi_lista.pop()
print(mi_lista[:])

# Suma listas
lista_3 = [1, 2, 3, 'a', 'b', 'c']
print(mi_lista + lista_3)

# Multiplica una lista
print(mi_lista * 3)
