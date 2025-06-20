#Programa para contar las palabras de un archivo
print("Programa para contar la cantidad de veces que se repite una palabra:\n")

nombre = "artículo.txt"
with open(nombre, "r", encoding = "utf-8") as archivo:
    contenido = archivo.read() #lee todas las lineas del texto
    
contenido = contenido.lower() #convierte a minúsculas todos las líneas del texto
palabra = contenido.split() #Separa las lineas en palabras
    
busqueda = input("Ingrese la palabra que desea buscar en el texto: ").lower() #Ingresa el usuario la palabra a buscar y se convierte en minuscula
conteo = palabra.count(busqueda) #cuenta las palabras
    
import textwrap #se usa para quitar la indentación del texto
    
print(textwrap.dedent(f"""
     ====================
     Contador de Palabras
     ====================
     
     Nombre del texto:  {nombre:<10}
     Palabra a buscar:  {busqueda:<10}
     Cantidad de palabras: {conteo:<10} 
"""))

    