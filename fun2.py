#Reescribiendo el ejemplo1 con funciones DEF
#FUNCION PROCIDIMENTAL: NO DEVUELVE RESULTADOS,
#Solo ejecuta una tarea.
def detectarTemperatura(lectura,consigna):
    if lectura == 17:
    #Acciones si es verdadero.
        print("La temperatura es igual 17")
        lectura=lectura+3
        print(f"temperatura: {lectura}")

    else:
    #Acciones si es falso.
        print(f"la temperatura no es igual a {consigna}")
        lectura=lectura-1
        print(f"temperatura: {lectura}")

detectarTemperatura(10,17)
detectarTemperatura(30,29)
detectarTemperatura(17,14)
detectarTemperatura(22,-4)
