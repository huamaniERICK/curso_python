# TIPOS DE DATOS ESTRUCTURADOS (TDA -  TIPOS DEE DATOS ABSTRACTOS)
```python
# listas: sus valores se puede actualizar, eliminar.
listas=["abel" ,20,5.2,.5,False,["texto" ,.2]]
# tupla: sus valores o elementos no pueden ser modificados o eliminados.
tupla=("abel" , 20,5.2, False,[])
# diccionarios o objetos
# los diccionarios almacenan los datos con clave:valor
diccionarios={"nombre":"antonio","edad":15 "sexo":False}
         # Clave:  # valor
```
-[!TIP]
-**Observacion:** que los tipos de datos estructurados pueden almacenar en su interior otros tipods de datos estructurados
```python
lista_alumnos:[{
    "nombre":"abel",
    "edad":20,
},{
    "nombre":"ruth",
    "edad":13,
},{
    "nombre":"jose ma",
    "edad":80,
},{
    "nombre":"rony",
    "edad":15,
}
]
```
## Metodos
### 1. convertir texto a lista
```python
texto="hola"
list(texto)
# ["h","o","l","a"]

# Metodo split"
texto="hola como estan alumnitos lindo"
texto.split(",")
# metodo join:Es el metodo para unir elementos de una lista de un solo texto
texto_largo="la vida es el arte de, dibujar sin borrar"
nuevo_texto=texto_largo.split(" ")
print(",".join(nuevo_texto))
```
### 2.agregar elementos al final de una lista 
````python
# metodo append= es el metodo que me permite agregar elemntos al fianl de una lista
lista["hola"]
lista.append("mundo")
print(lista)
# ["hola", "mundo"]

# metodo insert= es el metodo que me permite agregar elemento en cualquier ubicacion de mi lista
lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0,"antony")
````
### 3.eliminar elementos de una lista
```python
# metodo pop= es el metodo que elimina el ultimo elemento de una lista es el contrario de append
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop()

# primera manera - metodo remove=este metodo eliminael por el nombre el elemento que coincida dentro de una lista.elimina por nombre
lista_nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")

# segunda opcion-metodo pop = al pasarle por parametro un indice este lo elimina de la lista.elimina por indice
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop(0)
```
### 4.buscar un elemento de una lista
```python
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])

pertenencia="edith" in lista_nombres  # True False
```

### 5.comparacion  de listas
Podemos aser uso de los operadores de comparacion para comparar listas 
**ejem:** 

```python
compara=[1,2,3]>[1,2,4]
# 1 no porque son iguales en ambas listas
# 2 no porque son iguales en ambas listas
# 3 evalua que es menor que 4 
# entonces la primera lista es menor que la segunda lista
print(compara)
# salida:False
```

### 6.cuidado con las  copias
#### dato primitivo
```python
nombre="abel"
otro_nombre=nombre
print(id(nombre))
print(id(otro_nombre))
```
### 7. FE ERRADAS (Actualizar listas)
```python
lista=[1,3,4,5,6]
lista[0]=2
print(lista)
# [2,3,4,5,6,]
# modificado lista con diccionario
alumnos=[
    {
        "nombre":"abel",
        "edad":15
    },
    {
        "nombre":"anthony"
        "edad":29
    }
]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por definir"
print(alumnos)
```


### 9.ordenar una lista (sort)
esta funcion ordena una lista


### 10.metodo (copy)
copia el valor de la lista
