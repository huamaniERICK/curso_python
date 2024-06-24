#   FUNCIONES
## concepto
Matematicamente una funbcion es una operacion que toma uno o mas valores llamados`argumentos` y produce un valor denominado `resultado`.
> [!NOTE]
> Todos los lenguajes de programacion tiene funciones incorporadas (`funciones internas`), y funciones creadas por el usuario(`funciones externas`)
En programacion una funcion es un subprograma,es una estructura que nos permite agrupar codigo y sus principales objetivos son:
- `NO REPETIR` fragmentos de codigo 
- `REUTILIZAR` el codigo en distintos escenarios
## Estructura de una funcion
Una funcion viene `definida` por un `nombre`, sus `parametros` y su valor de `rertorno` .
una ves creada la funcion podremos solicitar su ejecucion `invocando` la funcion por su `nombre`
## definir una funcion en python
para definir una definicion en python primero utilizaremos la palabre reserva `def` seguida por el `nombre` de la funcion. A continuacion especificaremos los `parametros` con `()` si es una funcion sin parametros , `(a)` se es una funcion con parametros, si se tuviera mas de un parametro iran separados por `,`, finalizaremos l linea con `:` , en la siguiente linea sin olvidar el identado, comenzara el `cuerpo` de la funcion (microprograma) que puede obtener 1 o mas sentencias, finalmente devera `retornar` un resultado con la palabra reservada `return`.
> [!TIP]
> como retorno tambien se puede utilizar la `funcion interna`, `print()`, para depuracion de codigo no es recomendable usarlo en produccion.
> 
> `print` dentro de una funcion  es una herramienta que se utiliza para comprobar que una funcion que esta asiendo un trabajo de una manera correcta
> **ejemplo:**
```python
def saludo():
    saludo="hola mano"
    saludo_dos="como estas
    return f"{saludo}+{saludo_dos}"
    #print (f"{saludo}+{saludo_dos})
print(saludo())
# saludo()
```
# invocar una funcion 
para invocar , (o llamar , ejecutar ) una funcion solo tendremos que escribir el `nombre` de la funcion seguido por `()` parentesis. 
```python
def saludo ():
    print("hola")
# invocando la funcion 
saludo()
```
## Retornar un valor
Las funciones pueden retornar (o devolver) un valor .
```python
def uno ():
    return:
uno()
```
> [!WARNING]
> No confundir  `print` con `return`, el valor retornado por `return` nos permite usarlo fuera de su contexto. y `print()` solo mostrara el literal poir terminal.

## Retornando multiples valores 
El secreto es hacerlo mediante un tipo de dato estructurado
```python
def tupla ():
    return 2,3,4
varios()
# retorna (2,3,4)
def lista():
    return ["hola",45]
# retorna ["hola",45]
def dicc():
    return {"nombre":"jose","edad":45}
    dicc 
#retorna {"nombre":"jose","edad":45}
```

#### return
tipo de dato, tipo de dato estructurado
#### print
mensaje

## parametros y argumentos
si una funcion no dispusiera de valores de entrada estaria ilimitada en su actuacion es por ello que los `parametros` nos permiten variar los datos que consumen una funcion para obtener distintos resultados
**ejemplo**
* crear una funcion que recibe un valor numerico y retorna su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
sqrt(4)
```

cuando llamamos a una funcion con `argumentos` los valores de estos argumentos se copian en los correspondientes `parametros` dentro de la funcion.
```python
def ejem(a,b,c):
    return a+b+c
    ejm(4,5,6)
```

### Argumentos Nominales 
 en esta aproximacion los argumentos no son copiados en un orden  especifico si no que **se asignan por nombre a cada parametro**  ello nos permiten evitar el problema de conocer o recordar cual es el orden de los parametros en la definicion de la funcion.
 para utilizarlo basta con realixzar una asignacion de cada argumento de la propia llamada a la funcion.
 **ejemplo**
```python
def bulld_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia{familia}, con {num_core} cores y con una frecuencia de {frecuencia}
    """)
# Haciendo uso de argumentos nominales
bull_cpu(num_core=4, familia="intel", frecuencia=2.7)

```

### Argumentos Pocicionales
Los argumentos son copiados  en un orden especifico, en este caso debemos conocer o recordar cual es el orden de los parametros
**ejemplos**
```python
def bulld_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia{familia}, con {num_core} cores y con una frecuencia de {frecuencia}
    """)
# Haciendo uso de argumentos posicionales
build_cpu("intel",4,2.7)
```
## Parametros por defecto
Es pocible especificar **valores por defecto**  en los parametros de una funcion en el caso de que nos proporcione un valor al argumento en la llamada a la funcion, el parametro correspondiente tomaran el valor definido por defecto
**ejemplo**
```python
def alumnos(nombre,apellido,estado="aprobado"):

alumnos("ruth","castillo")
alumnos("anthony","cruzes","desaprobado")
```
## Desempaquetado/Empaquetado de argumentos(tarea)
El *desempaquetado y empaquetado de argumentos* en lenguajes de programación es una técnica que permite pasar múltiples argumentos a una función de manera más flexible y dinámica.
 
### El desempaquetado de argumentos 
  
- se refiere a pasar argumentos a una función como una lista o diccionario.

### El empaquetado de argumentos
- implica pasar argumentos a una función de manera desempaquetada, es decir, expandiendo una lista o diccionario en argumentos individuales.
 
## Partes
 
### 1. Empaquetado de Argumentos:
 
- Permite pasar múltiples argumentos a una función como una estructura única, como una lista o diccionario.
- Ayuda a simplificar la llamada a funciones con múltiples argumentos.
### 2. Desempaquetado de Argumentos:
 
- Permite pasar argumentos a una función desempaquetados, es decir, como argumentos individuales en lugar de una estructura única.
- Proporciona flexibilidad al llamar a funciones con argumentos almacenados en una lista o diccionario.
 
## Funciones
 
*- Empaquetado de Argumentos:*
 
- En Python, se puede realizar el empaquetado de argumentos utilizando el operador ` * ` para listas y  **  para diccionarios.
*Ejemplo en Python:*
```python

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```
*- Desempaquetado de Argumentos:*
 
- En Python, se puede realizar el desempaquetado de argumentos utilizando el operador ` * ` para listas y ` **`  para diccionarios.
*Ejemplo en Python:*
```python
 Copiar
def my_function(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_function(*my_list)
```
 
## Ejemplos
 
### Empaquetado de Argumentos:
 
- Enviar múltiples argumentos a una función como una lista:
```python
 
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```
### Desempaquetado de Argumentos:

- Pasar argumentos desempaquetados a una función desde una lista:
```
python
 Copiar
def my_function(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_function(*my_list)
```

 
### En resumen
 *el desempaquetado y empaquetado de argumentos* en lenguajes de programación como Python proporciona una forma conveniente de trabajar con funciones que requieren múltiples argumentos de manera flexible. ¡Es una técnica muy útil en el desarrollo de software! 

# Funciones internas de python (tarea)

- En Python, *las funciones internas* son aquellas que vienen integradas en el lenguaje y están disponibles para su uso sin necesidad de importar módulos externos. Estas funciones internas son ampliamente utilizadas en Python y proporcionan funcionalidades útiles para realizar diversas tareas. 
 
### Funciones Internas Comunes en Python:
 
*1.  `print()  ` : Utilizada para imprimir mensajes en la consola.*
 
```
python
 Copiar
print("Hola, mundo!")
```

*2.    `len()  ` : Devuelve la longitud de un objeto (número de elementos).*
 
```
python
 Copiar
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Salida: 5
```

*3.    `type()  ` : Devuelve el tipo de un objeto.*
 
```
python
 Copiar
x = 5
print(type(x))  # Salida: <class 'int'>
```

*4.    `input()  ` : Permite al usuario ingresar datos desde la consola.*
 
```
python
 Copiar
name = input("Ingrese su nombre: ")
```

*5.    `range()  ` : Genera una secuencia de números.*
 
python
 Copiar
for i in range(5):
    print(i)  # Salida: 0, 1, 2, 3, 4
 
*6.    `sum()  ` : Calcula la suma de elementos en una secuencia.*
 
```
python
 Copiar
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Salida: 15
```

*7.    `min()  `  y   ` max()  ` : Encuentran el valor mínimo y máximo en una secuencia.*
 
```
python
 Copiar
numbers = [10, 5, 8, 20]
print(min(numbers))  # Salida: 5
print(max(numbers))  # Salida: 20
```

*8.    `abs()  ` : Devuelve el valor absoluto de un número.*
 
```
python
 Copiar
x = -10
print(abs(x))  # Salida: 10
```
## tipos de funciones
### funciones anonimos (funciones lambda)
una funcion que no tiene nombre
`lambda:"hola"`
```python
lambda:"hola"
def saludo():
    return "hola"
```
### funciones closure
una funcion  que dentro tiene otra funcion
`def saludo(nombre):
        print(f"bienbenido{nombre}")
`
### funciones callback
funciones que reciben por parametro otra funcion
`int(input("ingrese un numero: "))`
### programacion funcional
La programacion funcional no requieere que sepas como se desarrrolla y ejecuta el procesamiento de la informacion
**ejemplo**
```python
lista=[5,7,8,4,1]
def num_minimo(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
        return minimo
print(min(lista))
# programacion funcional
```
#### averiguar sobre map(), filter(),reduce()

