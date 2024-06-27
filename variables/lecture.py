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

# lista=[5,7,8,4,1]
# def num_minimo(l):
#     minimo=l[0]
#     for n in l:
#         if n < minimo:
#             minimo=n
#     return minimo
# print(min(lista))

# map
lista=[4,7,8,5,2]
nueva_lista=list(map(lambda x:x+1,lista)) # por defecto retorna map)
print(nueva_lista)

# tengo una lista de alumnos que todos ellos aprobaron y pasan al 3er semestre
# en mi lista todos estan con el 2do semestre por lo que tendremos que crear una solucion que 
# que cambie el campo de semestre de 2 a 3
lista_alumnos=[
    {
        "nombre":"abel",
        "edad":36,
        "semestre":2
    },
    {
        "nombre":"anthony",
        "edad":40,
        "semestre":2
    },
    {
        "nombre":"edith",
        "edad":50,
        "semestre":2
    }
]
def objeto(e):
    if "semestre" in e:
        e["semestre"]=e["semestre"]+1
    e["especialidad"]="arquitectura"
    return [
            e
        ]
nueva_lista=list(map(objeto , lista_alumnos))
print(nueva_lista)

#devolver los numeros pares de una lista
lista_numeros=[4,8,2,5,7,10,6,5,3,20]
nueva_lista=list(filter(lambda x: x%2==0, lista_numeros))
print(nueva_lista)

lista_alumnos=[
    {
        "nombre":"abel",
        "edad":36,
        "semestre":2
    },
    {
        "nombre":"anthony",
        "edad":40,
        "semestre":2
    },
    {
        "nombre":"edith",
        "edad":50,
        "semestre":2
    }
]
otra_lista=list(filter(lambda x: x["edad"]<50, lista_alumnos) )
print(otra_lista)

# TAREA
# crear una lista de alumnos  con los siguientes campos
# nombre, apellido, edad, celular, email
# 1= actualizar  los registros con un campo mas todos tendran el campo de estudio de programa de estudio e enfermeria
# 2=buscar el segundo registro y actualizar  sus edad a 50 años

lista_alumnos = [
    {
        "nombre": "erick",
        "apellido": "Pérez",
        "edad": 35,
        "celular": "123456789",
        "email": "erick@example.com"
    },
    {
        "nombre": "percy",
        "apellido": "García",
        "edad": 49,
        "celular": "987654321",
        "email": "percy@example.com"
    },
    {
        "nombre": "ronal",
        "apellido": "Rodríguez",
        "edad": 55,
        "celular": "456789123",
        "email": "ronal@example.com"
    }
]

# Función para agregar el campo 'programa'
def agregar_programa(e):
    e["programa"] = "enfermería"
    return e

# Actualizar todos los registros con el campo 'programa'
lista_alumnos_actualizada = list(map(agregar_programa, lista_alumnos))

# Actualizar la edad del segundo registro a 50 años
lista_alumnos_actualizada[1]["edad"] = 50

# Imprimir la lista actualizada
print(lista_alumnos_actualizada)