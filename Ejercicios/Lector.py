try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        print("Lista de Productos:\n")
        for linea in archivo:
            linea = linea.strip()
            datos = linea.split(',')
        
        if len(datos) == 3:
         nombre, precio, cantidad = datos
         print(f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")
         
        else:
            print("Línea con formato incorrecto:", linea)
    
except FileNotFoundError:
    print("No se encontró el archivo 'productos.csv'. Asegúrate de que exista en el directorio.")