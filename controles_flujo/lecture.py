# este codigo imprime numeros

for n in range(1,11):
    print(n)
#primer ejemplo if estructurado
edad=int(input("ingrese tu edad: "))
if edad>=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

#segundo ejemplo if almacenado en variable
edad_dos:int=int(input("ingrese su edad: "))
respuesta:str="eres mayor" if edad_dos>=18 else "eres menor"
print(respuesta)

# crear un programa que me imprima los 5 vocales
vocales:str="aeiou"
for n in range(0,5):
    print(vocales[n])

#crear un programa que te muestre los 8 primeros numeros pares 
contador=0
for n in range(1,17):
    if n%2==0:
        contador+=1
        print(f"{n} es par numero {contador}")
    
#crear un programa que pida al usuario escribir una oracion 
#y mostrar por terminal la cantidad de vocales "a" que tiene esa oracion
#ojo solo las "A" minuscula
oracion:str=input("escribe una oracion: ")
contador:int=0
for n in range(0,len(oracion)):
    if oracion[n]=="a":
        contador=contador+1
print(f"la cantidad de letras a es {contador}")



for ind_vocal,let_vocal in enumerate("aeiou"):
    print(f"el indice es {i} y la letra es {l}")
print(f"la cantidad de letras a que tengo es {contador}")

#crear un programa que me cuente la cantidad de comas de una oracion  y me muestre indices.
contador=0
oracion:str=input("escribe la oracion:")
for n in range(0,len(oracion)):
    if oracion [n]==",":
        contador+=1
        print(f"la coma fue encontrada en el indice {n}")
print("la cantidad de comas encontradas es ",(contador))
    

