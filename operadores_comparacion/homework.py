#1 DISEÑAR UN ALGORITMO QUE DETERMINE SI EL PRIMERO DE 2 NUMEROS ES EL MAYOR
numero_1=float=input("ingrese primer numero: ")
numero_2=float=input("ingrese segundo numero: ")
comparacion=numero_1 > numero_2
if comparacion:
    print("el primer numero es mayor")
else:
    print("el primer numero es menor")

#3 ALGORITMO QUE VALIDE SI UN NUMERO SE ENCUENTRA EN EL RANGO DE 1 A 100
numero=int(input("ingrese el numero: "))
if numero >=1 and numero <= 100:
    print("el numero esta entre el rango de 1, 100")
else:
    print ("el numero no se encuentra dentro del rango")


#7 ALGORITMO QUE VALIDE SI UN NUMERO ES PRIMO O NO 
numero=int(input("ingrese un numero: "))
if numero%2!=0:
    print("el numero ingresado no es primo")
else:
    print("el numero ingresado es primo")


#8 ALGORITMO QUE COMPARE SI 2 NUMEROS SON IGUALES O DIGERENTES O SI UNO ES EL DOBLE QUE EL OTRO.
numero1=int(input("ingrese primer numero: "))
numero2=int(input("ingrese segundo numero: "))
if numero1==numero2:
    print("los numeros son iguales")
if numero1!=numero2:
    print("los numeros son diferentes")
print(numero1 *2==numero2)