#Solicitando datos al usuario
nombre=input("Ingresa tu nombre:")
apellido=input("Ingresa tu apellido:")
edad=input("Ingresa tu edad:")
salario=input("Ingresa tu salario:")

#Formatear los datos en una linea
linea=f"{nombre},{apellido},{edad},{salario}\n"

#Solicitando el nombre al archivo
ruta=input("Nombre del archivo:")

#Guardar los datos en un archivo
with open(ruta,"a") as archivo:
    archivo.write(linea)
    
print("Datos guardados correctamente en",ruta)