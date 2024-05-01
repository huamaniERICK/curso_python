#4  LOS ALUMNOS DE UN CURSO SE HAN DIVIDIDO EN DOS GRUPOS A Y B  DE ACUERDO AL SEXO Y EL NOMBRE . EL GRUPO A ESTA FORMADO POR LAS MUJERES CON UN NOMBRE ANTERIOR A LA M
# Y LOS HOMBRES CON UN NOMBRE POSTERIOR A LA N Y EL GRUPO B POR EL RESTO.
# ESCRIBIR UN PROGRAMA QUE PREGUNTE AL USUARIO SU NOMBRE Y SEXO , Y MUESTRE POR PANTALLA EL GRUPO  QUE LE CORRESPONDE.
nombre=str(input("ingrese su nombre: "))
sexo=str(input("ingrese su sexo(masculino/femenino): "))
if (nombre <"m" and sexo == "femenino") or (nombre>"n" and sexo =="masculino"):
    grupo="A"
else:
    grupo="B"
print("usted pertenece al grupo",grupo)


#5  Escribir un programa para una empresa que tien salas de juegos para todas las edades y quiere cacular de forma automatica el precio que debe cobrar a sus clientes por entrar.
# el programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada .
# si el cliente es menor de 4 años puede entrar gratis , si tiene entre 4 y 18 años debe pagar S/5 y si es mayor de 18 años , S/ 10.
edad=int(input("por favor ingrese su edad: "))
if edad <4:
    print("puede ingresar sin pagar")
if edad >=4 and edad <18:
    print("usted tiene que pagar un monto de S/ 5")
if edad >18:
    print("usted tiene que pagar por su edad un monto de S/10")