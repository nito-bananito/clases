#Programa principal

#Importando modulo
import funciones as md
from funciones import divicion,suma,multiplicacion

print("Programa con las operaciones basicas")
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
print(f"La resta es: {md.resta(num1,num2)}")
respuesta=divicion(num1,num2)
respuesta2=suma(num1,num2)
respuesta3=multiplicacion(num1,num2)
print("El resultado de la division es:",respuesta)
print("El resultado de la suma es:",respuesta2)
print("El resultado de la multiplicacion es:",respuesta3)
print(md.texto)