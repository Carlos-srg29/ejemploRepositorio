#Reescribiendo el ejemplo1 con funciones DEF
#FUNCION RETORNA DATOS

def detectarTemperatura(lectura,consigna):
    if lectura == consigna:
        return True
    else:
    #Acciones si es falso.
        return False

detectarTemperatura(10,17)
print(detectarTemperatura(30,29))
if detectarTemperatura(17,14):
    print("el resultado es verdadero")
else:
    print("el resultado es falso")
resultado=detectarTemperatura(22,-4)
print(f"El resultado es {resultado}")
