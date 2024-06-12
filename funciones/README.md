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

## Funciones Internas de python (tarea)

