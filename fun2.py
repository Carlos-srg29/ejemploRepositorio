#Reescribiendo el ejemplo1 con funciones DEF
#BLOQUE IF
def detectarTemperatura(lectura):
    if lectura == 17:
    #Acciones si es verdadero.
        print("La temperatura es igual 17")
        lectura=lectura+3
        print(f"temperatura: {lectura}")

    else:
    #Acciones si es falso.
        print("la temperatura no es igual a 17")
        lectura=lectura-1
        print(f"temperatura: {lectura}")

detectarTemperatura(10)
detectarTemperatura(30)
detectarTemperatura(17)
detectarTemperatura(22)
