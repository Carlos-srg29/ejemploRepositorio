name=input("Ingresa un nombre de animal en plural")
archivo = open("mi_archivo.txt","a")
archivo.write(f"Tres tristes tigres {name} \n")
archivo.close()
