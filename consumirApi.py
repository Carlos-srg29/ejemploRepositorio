import requests
#import urllib3

#Desactivar las advertencias de certificados no seguros (comun en IPs locales con https)urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "http://10.121.16.118:7010/api/enviar"

# Los datos que deseas enviar segun tu ejemplo
payload = {
    "imagen": [102, 153, 129, 129, 129, 66, 36, 24]
}

print("Enviando datos a la API...")

try:
    # Enviamos la peticion POST. verify=False evita errores por certificados SSL locales
    respuesta = requests.post(url, json=payload, verify=False)
    
    print(f"Codigo de estado del servidor: {respuesta.status_code}")
    
    if respuesta.status_code:
        print("¡Datos enviados con exito!")
        try:
            print("Respuesta del servidor:", respuesta.json())
        except ValueError:
            print("Respuesta del servidor (Texto):", respuesta.text)
    else:
        print("El servidor rechazo la peticion.")
        print("Detalle del error:", respuesta.text)

except requests.exceptions.ConnectionError:
    print("Error: No se pudo establecer conexion con la IP 10.121.16.118.")
    print("Por favor, verifica que el servidor este encendido y que estes en la misma red local.")
