#9 ALGORITMO QUE CALCULE EL AREA DE UN CUADRADO
lado=float(input("ingrese el lado del cuadrado: "))
area=lado * lado
print("el area del cuadrado es: " +str (area))


#10 ALGORITMO QUE CONVIERTA KILOMETROS A MILLAS
kilometros=float(input("ingrese cantidad de kilometros: "))
millas= kilometros * 0.621371
print("la cantidad de millas es " +str(millas))


# 1 ESCRIBIR UN PROGRAMA  QUE PREGUNTA EL NOMBRE DEL USUARIO EN LA CONSOLA Y NUMERO ENTERO E IMPRIMA POR PANTALLA EN LINEAS DISTINTAS EL NOMBRE DEL USUARIO TANTAS VECES COMO EL NUMERO INTRODUCIDO
NOMBRE=(input("ingrese nombre del usuario: "))
numero_entero=int(input("ingrese numero entero: "))
print((NOMBRE+"\n")*numero_entero)



# 2  ESCRIBIR UN PROGRAMA QUE PREGUNTE EL NOMBRE COMPLETO DEL USUARIO EN LA CONSOLA Y DESPUES MUESTRE POR PANTALLA EL NOMBRE COMPLETO DEL USUARIO 3 VECES
NOMBRE_COMPLETO=(input("INGRESE SU NOMBRE COMPLETO: "))
NUMERO=3
print((NOMBRE_COMPLETO+"\n")*NUMERO)


# 3 LOS TELEFONOS DE UNA EMPRESA TIENEN EL SIGUIENTE FORMATO:
#PREFIJO-NUMERO-EXTENCION DONDE EL PREFIJO ES EL CODIGO DE PAIS +34, Y LA EXTENCION TIENE 2 DIGITOS (EJEMPLO)
# +34-913724710-56. ESCRIBIR UN PROGRAMA QUE PREGUNTE POR UN NUMERO DE TELEFONO CON ESTE FORMATO Y MUESTRE POR PANTALLA EL NUMERO DE TELEFONO SIN EL PREFIJO Y LA EXTENCION
prefijo=str=int(input("ingrese el prefijo o codigo de su pais: "))
numero_telefonico=str=int(input("ingrese el numero de telefono: "))
extencion=str=int(input("ingrese la extencion: "))
numero_unido=prefijo+numero_telefonico+extencion
print(numero_unido)
print(numero_telefonico)