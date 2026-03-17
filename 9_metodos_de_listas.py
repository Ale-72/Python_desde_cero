#Metodos de Listas
numeros = [1, 2, 3, 4, 5]

#Adicionar elementos a una lista
numeros.append(6)
print(numeros)
#Insertar elementos en una posicion determinada
numeros.insert(0, -1)
print(numeros)

numeros.insert(1, 0)
print(numeros)

#Eliminar un elemento en su primera aparicion
numeros.remove(1)
print(numeros)

#Verificar si un elemento existe en la lista
print(4 in numeros)

#Tamaño de la lista
print(len(numeros))

#Elimina el contenido de la lista
numeros.clear()
print(numeros)