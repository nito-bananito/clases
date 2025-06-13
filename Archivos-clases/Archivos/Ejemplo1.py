#Ejemplificar creacrión de archivos en python

#Declarar un objeto de tipo archivo
archi1=open("datos.txt","a")
archi1.write("Cuarta linea\n")
archi1.write("Quinta linea\n")
#archi1.write("Tercera linea\n")
archi1.close
print("Final del programa")