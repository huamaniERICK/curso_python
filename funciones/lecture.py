# return devuelve valores que puedo aser uso
# crear una funcion que retorne el numero 10 y muestra terminal si es par
# siempre que el valor retorne mi funcion se utilize en mas sentencia u operaciones hacer uso de return
def dies():
    return 10
if dies()%2==0:
    print("es par")
else:
    print("es impar")
# print solo muestra por terminal

# crear una funcion que me muestre del prodeducto de 2 numeros
def producto (a,b):
    return a*b
# crear una lista que me retorne una lista de 3 numeros
def lista_numeros():
    return [1,2,3]



# print usaremos cada ves que muestra funcion retorne en un mensaje
# crear una funcion que por parametro  reciba un nombre y retorne un mensaje de bienbenida con el nombre

def mensaje(nombre):
    print(f"hola, {nombre}, bienbenido ala fiesta")
mensaje("juan")


# crear una funcion que reciba por parametro una lista de numeros y me devuelva el numero menor
# mostrar por terminal el valor  retornando por la funcion
lista_numeros=[4,6,4,3,7,4,1,10]
def min(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
print(min(lista_numeros))


# crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debera retornar
# un diccionario con los datos luego mostrar por terminal el valor de retorno de mi funcion
nombre="erick"
edad=20
def persona(nom,edad):
    return dict(
        nombre=nom,
        edad=edad
    )
print(persona(nombre,edad))