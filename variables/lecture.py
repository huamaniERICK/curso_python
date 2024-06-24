# # ejemplo lambda
# saludo=lambda n,a:f"hola,{n},{a}"
# print(saludo("ruth","castillo"))
# # crear un programa anonimo que reciba como parametro una lista de 5 numeros y retorne dos listas 
# # una con los numeros pares y una con numeros impares

# lista=[1,2,3,4,5,6,7,8,9,10] 
# pares=lambda l:[n for n in lista if n%2==0]; impares=lambda l:[n for n in lista if n%2!=0]
# print(pares(lista))
# print(impares(lista))

# # funciones callbak
# int(input())
# def mensaje(m):
#     print(m)
# def pedir_nombre():
#     nombre=input("ingresa tu nombre")
#     return nombre
# mensaje(pedir_nombre)

lista=[5,7,8,4,1]
def num_minimo(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
print(min(lista))
    