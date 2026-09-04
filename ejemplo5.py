#MODIFICAR PARA LEER 2 NUMEROS POR TECLADO.
#Y OPERAR: 1=> suma, 2=>, 3=> multiplicacion
#LECTURA DE LOS NUMEROS
num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa el segundo numero: "))

#SELECCION DE LA OPCION
opcion= int(input("1=> suma, 2=>, 3=> multiplicacion"))
match opcion:
    case 1:
        resultado = num1 + num2
        print (f"La suma de {num1} + {num2} es: {resultado}")
    case 2:
        resultado = num1 - num2
        print(f"La resta de {num1} - {num2} es: {resultado}")
    case 3:
        resultado = num1 * num2
        print (f"La multiplicacion de {num1} * {num2} es: {resultado}")
    case _:
        print(f"Opcion invalidad: {opcion}")