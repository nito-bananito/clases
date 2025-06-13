def calcPago(precio, cant):
    return precio*cant
def main():
    productos=[]
    precios=[]
    cantidades=[]
    totales=[]
    resp="SI"
    while resp.upper() !="NO":
        producto=input("Producto: ")
        precio=float(input("Precio: "))
        cantidad=float(input("Cantidad: "))
        total=calcPago(precio, cantidad)
        
        productos.append(producto)
        precios.append(precio)
        cantidades.append(cantidad)
        totales.append(total)
        
        print("Desea agregar otro producto Si-No")
        resp=input("Respuesta ")
        
    print(f'\n {"Factura":^40}')
    print(f'{"Producto":<10}',f'{"Precio":>10}', f'{"Cantidad":>10}', f'{"Total":>10}')
    tam=len(productos)
    for i in range(tam):
        print(f"{productos[i]:<10} {precios[i]:10} {cantidades[i]:10} {totales[i]:10}")
        
    monto=sum(totales)
    print("Total a pagar C$: ",monto)

main()