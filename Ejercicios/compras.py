# Paso 1: Abrir el archivo compras.txt en modo de escritura para iniciar una nueva lista
with open("compras.txt", "w", encoding="utf-8") as archivo:
    print("Generador de Lista de Compras")
print("Escribe los productos uno por uno.")
print("Cuando termines, escribe 'fin' para guardar la lista.\n")

# Paso 2: Crear un bucle infinito
while True:
    producto = input("Producto: ")
    if producto.strip().lower() == "fin":
        break

archivo.write(producto + "\n")

print("Tu lista de compras ha sido guardada en 'compras.txt'.")