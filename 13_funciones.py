#Funciones -> Son bloques de codigo que realiza una tarea especifica y que son reutilizables
def saludar():
    print("Hola, bienvenidos al curso de Python")
    
#Funcion con parametros
def saludo(nombre):
    print("Hola, "+nombre+" bienvenido a clses")
    
#Funcion que devuelve valores
def suma(a, b):
    return a + b

#Establecer valores por defecto para los parametros de la funcion
def bienvenida(nombre="Estudiante"):
    print("Bienvenido ",nombre)
    
#Funcion con argumentos variables
def sumador(*args):
    return sum(args)

#Llamada a la funcion
saludar()
saludo("Bruno Diaz")
resultado = suma(10, 4)
print("La suma es: ", resultado)
bienvenida()
bienvenida("Susana")
print(sumador(1, 2, 3, 4, 5))
print(sumador(4, 5, 6))