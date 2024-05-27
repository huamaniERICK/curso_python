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
