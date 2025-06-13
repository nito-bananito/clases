#Pidiendole al usuario el nombre de la carpeta
ruta=input("Escriba el nombre del archivo:")
archi1=open(ruta,"a")

try:
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    print(f"El archivo tiene {len(lineas)} líneas.")

except FileNotFoundError:
    print("No se encontró el archivo. Asegúrate de escribir bien el nombre.")