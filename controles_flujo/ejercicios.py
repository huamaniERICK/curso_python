
# escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad=int(input("ingrese su edad: "))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("aun no eres mayor de edad")


#escribir un programa que almacene la cadene de caracteres de contraseña en un variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
#introducida por el usuario coincide con la guardad en la variable sin tener en cuenta mayusculas y minuscula.
contraseña="blachat"
contraseña_mayuscula =""
for letra in contraseña:
    codigo_ascii = ord (letra)
    if 97 <= codigo_ascii <=122:
        codigo_ascii -=32
        contraseña_mayuscula += chr(codigo_ascii)
        print("contraseña en mayusculas:",contraseña_mayuscula)

#Escribir un programa que pida al usuario un numero entre positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero 
#separado por comas.
numero=int(input("ingrese un numero: "))
resultado=""
for i in range(numero, -1, -1):
    resultado += str(i)
    if i >0:
        resultado += ","
print(resultado)


