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
    
# crear un programa que pida al usuario escribir una oracion 
# y mostrar por terminal la cantidad de vocales "a" que tiene esa oracion
# ojo solo las "A" minuscula
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
print((contador),"es el total de comas encontradas en la oracion")


# programa ejecutado con el enumerate   
oracion:str=input("ingrese la oracion: ")
contador:int=0
for indice,letra in enumerate(oracion):
    if letra==",":
        print(f"su indice es {indice}")
        contador+=1
print(f"la cantidad de comas es {contador}")

# ESCRIBIR UN PROGRAMA QUE PREGUNTE AL USUARIO SU EDAD Y MUESTRE POR PANTALLA TODOS LOS AÑOS QUE HA CUMPLIDO (DESDE 1 HASTA SU EDAD)
edad=int(input("ingrese su edad: "))
for i in range(1, edad+1):
    print("has cumplido",i,"años")

# CREAR UN PROGRAMA QUE PIDA EL NOMBRE DE 3 PERSONAS Y GUARDE EN UNA VARIABLE GLOVAL LAS ULTIMAS LETRAS DE SUS NOMBRES.
#MOSTRAR POR PANTALLA LA VARIABLE GLOBAL CON LAS 3 ULTIMAS LETRAS DEL NOMBRE DE CADA PERSONA
ultima_letra:str=""
for _ in range(3):
    nombre:str=input("escribe tu nombre: ")
    last_letter:str=nombre[-1]
    ultima_letra+=last_letter
print(ultima_letra)

# crear un programa que muestre por terminal las siguiente figura:
# a 
# ee
# iii
# oooo
# uuuuu
vocales="aeiou"
for i in range(len(vocales)):
    figura=vocales[i]*(i+1)
    print(figura)
# crear un programa