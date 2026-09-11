import deteccionDeTemperatura
test = deteccionDeTemperatura.detectarTemperatura(17,22)
print (f"El resultado es: {test}")

print(deteccionDeTemperatura.sumaDeNumeros(34,56))

parametro = deteccionDeTemperatura.sumaDeNumeros(23,-86)
otrotest=deteccionDeTemperatura.detectarTemperatura(parametro,-7)
print(f"resultado final: {otrotest}")