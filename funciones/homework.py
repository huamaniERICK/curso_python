# # crear una funcion que reciba por argumento n numeros y retorne una lista con los numeros pares
# def num_pares(*args):
#     lista_pares=[]
#     for n in args:
#         if n%2==0:
#             lista_pares.append(n)
#     return lista_pares
# print(num_pares(8,5,4,7,9,25,4,7,12))
# por comprencion
#  return [n for n in args] 


# crear 3 funciones para los siguientes casos 
# calcular el numero menor
# calcular el numero mayor
# calcular la suma de todos los nnumeros
# se le pasar por argumentos n numeros

def Min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor
def Max(*args):
    mayor=args[0]
    for n in args:
        if n>mayor:
            mayor=n
    return mayor
def Sum(*args):
    suma=0
    for n in args:
        suma+=n
    return suma

valores=4,7,8,5,2,1
print(Min(*valores))
print(Max(*valores))
print(Sum(*valores))
