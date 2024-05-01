#2 algoritmo que calcule el promedio de 3 numeros
numero1=int(input("ingrese primer numero: "))
numero2=int(input("ingrese segundo numero: "))
numero3=int(input("ingrese tercer numero: "))
promedio=(numero1+numero2+numero3)/3
print(promedio)
if promedio >13:
    print("aprobado")
else:
    print("desaprobado")


#6 ALGORITMO QUE DETERMINE UN VIAJE DE IDA Y VUELTA AL SOL A UNA VELOCIDAD CONSTANTE IGUAL AL DE LA LUZ
velocidad_luz=299792458
distancia_ida=149597870700
tiempo_ida=distancia_ida / velocidad_luz
tiempo_vuelta=distancia_ida / velocidad_luz
tiempo_total=tiempo_ida + tiempo_vuelta
print("el tiempo total del viaje de ida y vuelta al sol es de:")
print("segundos: ", tiempo_total)
print("minutos:" , tiempo_total/60)
print("horas:" ,tiempo_total/3600)


# 1 ESCRIBIR UN PROGRAMA  QUE PREGUNTA EL NOMBRE DEL USUARIO EN LA CONSOLA Y NUMERO ENTERO E IMPRIMA POR PANTALLA EN LINEAS DISTINTAS EL NOMBRE DEL USUARIO TANTAS VECES COMO EL NUMERO INTRODUCIDO
NOMBRE=(input("ingrese nombre del usuario: "))
numero_entero=int(input("ingrese numero entero: "))
print((NOMBRE+"\n")*numero_entero)


# 2  ESCRIBIR UN PROGRAMA QUE PREGUNTE EL NOMBRE COMPLETO DEL USUARIO EN LA CONSOLA Y DESPUES MUESTRE POR PANTALLA EL NOMBRE COMPLETO DEL USUARIO 3 VECES
NOMBRE_COMPLETO=(input("INGRESE SU NOMBRE COMPLETO: "))
NUMERO=3
print((NOMBRE_COMPLETO+"\n")*NUMERO)

