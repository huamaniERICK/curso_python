# STRING (cadena de texto)
Es una secuencia de caracteres encerrada entre comillas simples ` (")` o comillas dobles `("")`.
Los strings se utilizan para representar texto en un programa. puede contener letras, numeros, simbolos y espacios en blanco
>ejemplo
```python
mensaje="hola, ¿como estas?"
```
en este ejemplo, la variable `mensaje` contiene un string que representauna frase de saludo.
Los string en python son inmutables, lo que significa que una vez que se crea un string no se puede modificar directamente, sin embargo puedes realizar diversas operaciones y manipulaciones en los strings, como concatenarlos , dividirlos, obtener su longitud, acceder a caracteres individuales, entre otros.
> ejemplo
```python
saludo = "Hola"
nombre = "Erick"

# 1:concatenacion de strings
mensaje = saludo +","+nombre + "!"
print(mensaje)   
#imprime "Hola, Erick!"

#2: obtener una longitud de un strings
longitud = len(saludo)
print(longitud)  
 # imprime 4

#3: acceder a caracteres individuales
primer_caracter = saludo[0]
print(primer_caracter) 
 # imprime "H"

#4: Reemplazar parte de un string
nuevo_mensaje = mensaje.replace("Erick","maria")
print(nuevo_mensaje) 
 # imprime "Hola, maria!"
