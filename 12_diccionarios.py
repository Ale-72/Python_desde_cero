#Diccionarios -> Almacena pares de clave-valor
mi_diccionario = {"nombre": "Bruno Diaz", "edad": 25, "Ciudad": "La Paz"}
print(mi_diccionario)

#Acceder a un valor
print(mi_diccionario["nombre"])
print(mi_diccionario["Ciudad"])

#Agregar elementos
mi_diccionario["profesion"] = "Ingeniero"
print(mi_diccionario)

#Eliminar un elemento
del mi_diccionario["Ciudad"]
print(mi_diccionario)

#Obtener claves del diccioanrio
print(mi_diccionario.keys())

#Obtener valores del diccioanrio
print(mi_diccionario.values())

#Verificar si una clave existe
if "edad" in mi_diccionario:
    print("Clave encontrada")
    
#Recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[Clave: ]", clave, "[Valor: ]", valor)