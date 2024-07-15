# averiguar modulos y paquetes en python
## MODULO
es un conjunto de funciones
un archivo `.py` con funciones

Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python, como funciones, variables y clases.
Los módulos permiten organizar el código en archivos separados para facilitar su mantenimiento y reutilización.
Para utilizar un módulo en un programa Python, se puede importar utilizando la palabra clave  `import` .
Ejemplo de importación de un módulo:
> ejemplo
```python
Copiar
import modulo
```
Una vez importado, se pueden acceder a las funciones y variables definidas en el módulo utilizando la notación de punto, por ejemplo:  `modulo.funcion()`

1. Creamos un archivo llamado  operaciones.py  con el siguiente contenido:
 
```python
 Copiar
# operaciones.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
```

2. Luego, en otro archivo Python, podemos importar y utilizar este módulo de la siguiente manera:
 
```python
 Copiar
import operaciones

print(operaciones.suma(5, 3))  # Salida: 8
print(operaciones.resta(10, 4))  # Salida: 6

```

## PAQUETE
es una carpeta con una serie de archivos `.py`
una carpeta con modulos de python

 
-Un paquete en Python es una forma de estructurar jerárquicamente módulos relacionados.

-Los paquetes son directorios que contienen uno o más módulos y un archivo especial  _init_.py  que indica que el directorio es un paquete de Python.

-Los paquetes permiten organizar y agrupar módulos relacionados en una estructura de directorios.

-Para importar un módulo de un paquete, se utiliza la notación de punto para indicar la estructura jerárquica.

Ejemplo de importación de un módulo de un paquete:
>ejemplo
```python
Copiar
import paquete.modulo
```
1. Creamos una estructura de directorios de la siguiente manera:
 

``` Copiar
matematicas/
    _init_.py
    operaciones.py
    multiplicacion.py
 
```
2. En el archivo  operaciones.py , tenemos las mismas funciones de suma y resta como en el ejemplo anterior.
3. Creamos un nuevo archivo  multiplicacion.py  con el siguiente contenido:
 
```python
 Copiar
# multiplicacion.py

def multiplicacion(a, b):
    return a * b
 
``` 
4. En el archivo  _init_.py  del paquete  matematicas , podemos importar los módulos para que estén disponibles al importar el paquete:
 
```python
 Copiar
# _init_.py

from . import operaciones
from . import multiplicacion
 
``` 
5. Luego, en otro archivo Python, podemos importar y utilizar los módulos del paquete  matematicas  de la siguiente manera:
 
```python
 Copiar
from matematicas import operaciones, multiplicacion

print(operaciones.resta(10, 5))  # Salida: 5
print(multiplicacion.multiplicacion(3, 4))  # Salida: 12
```
# diferencias enytre modulos y paquetes
### modulo

-un módulo en Python es un archivo individual que contiene código, 

-Los módulos se utilizan para organizar el código a nivel de archivo
### paquete
-un paquete es una colección de módulos organizados en una estructura de directorios. 

-los paquetes se utilizan para organizar módulos relacionados en una estructura de directorios para facilitar la modularidad y la reutilización del código en proyectos más grandes.
## MODULOS
El codigo dentro de mi archivo es un 