#Modificar para que en cada interacion inserte una nueva linea en un archivo
import keyboard
import time
archivo=open("mi_archivo.txt","w")
linea=0
while True:
    print("😈​ ​***\n")
    archivo.write(f"{linea} ===> ******** ​\n")
    linea +=1
    if keyboard.is_pressed('esc'):
        print("\n¡Tecla 'Esc' detectada. Bucle detenido.")
        
        break
    # Tu lógica dentro del bucle
    print("Procesando...", end="\r")
    time.sleep(0.1)
archivo.close()