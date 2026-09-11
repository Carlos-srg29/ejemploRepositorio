#Reescribiendo el ejemplo1 con funciones DEF
#Creando una libreria

def detectarTemperatura(lectura,consigna):
    if lectura == 17:
    #Acciones si es verdadero.
        print("La temperatura es igual 17")
        lectura=lectura+3
        print(f"temperatura: {lectura}")

#Implementar una funcion que sume 2 numeros, devuelve suma.
def sumaDeNumeros(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

resultado = sumaDeNumeros(34,56)
print(f"La suma es: {resultado}") 