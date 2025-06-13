#Ejemplificar lectura de un archivo

#Crea la variable para manipular el archivo
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()

#Agragando dos lineas más
archi1=open("datos.txt","r+")
contenido=archi1.read()
print(contenido)
archi1.write("otra linea 1\n")
archi1.write("otra linea 2\n")
archi1.close()