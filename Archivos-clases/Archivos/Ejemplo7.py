with open("datos.txt","r",encoding="utf-8") as archivo:
    lineas=archivo.readlines()
    
#Filtrar las lineas que no contienen "Segunda linea"
lineas_filtradas=[linea for linea in lineas if linea.strip() != "otra linea 1"]

#Sobrescribir el archivo con las linea filtradas
with open("datos.txt","w",encoding="utf-8") as archivo:
    archivo.writelines(lineas_filtradas)