import keyboard
import time

porcentaje=0
while porcentaje < 100:
    porcentaje += 25 #Incrementar en 25 a la variable
    print(f"Cargando... {porcentaje}%")
print("Descarga completa!")

#Implementar un buble que se de detenga
#cuando la tecla pulsada es "ESCape"
print("El bucle está corriendo Presiona 'Esc' para detenerlo.")

while True:
    # Verifica si se presionó la tecla Escape
    if keyboard.is_pressed('esc'):
        print("\n¡Tecla 'Esc' detectada! Deteniendo el bucle")
        break
    
    # Tu lógica dentro del bucle
    print(".", end="", flush=True)
    time.sleep(0.1) # Pausa corta para no saturar la CPU