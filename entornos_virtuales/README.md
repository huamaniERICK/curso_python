# PASOS PARA CREAR UN ENTORNO VIRTUAL

## PASO 1
crear una carpeta en donde podremos ubicar nuestro entorno virtual.

**mkdir entorno_virtual**
## paso 2
ingresar a nuestro archivo creado con el comando `cd (nombre de la carpeta creada)`.

**cd entorno_virtual**

## PASO 3
despues de ingresar colocamos el siguiente comando.
python -m venv .`nombre de la carpeta qu quieres crear`.

**python -m venv .ganadores**
## PASO 4
ingresamos el siguiente comando para activar la carpeta creada `source .nombre de la carpeta creada/scripts/activate`.

**source .ganadores/scripts/activate**

**(.ganadores)**
## PASO 5
colocar el comando `pip install (nombre del paquete que quieres desacargar)`

**pip install flet**

## PASO 6
colocar el comando `pip list` para poder ver la version y ver si se instalo correctamente el paquete.

$ pip list
Package    Version
---------- -------
pip        24.0
setuptools 65.5.0

[notice] A new release of pip is available: 24.0 -> 24.1.2
[notice] To update, run: `python.exe -m pip install --upgrade pip
(.venv)`

## PASO 7
para actualizar la version del paquete se copia el comando que que ya nos indico en el paso 6
**python.exe -m pip install --upgrade pip
(.venv)**
## PASO 8
ahora podremos ver el paquete actualizado con el comando `pip --version`

**pip --version**
## PASO 9
al final tenemos que verificar con el comando `pip list` y nos aparecera de la siguiente forma

**$ pip --version
pip 24.1.2 from C:\Users\Erick\Desktop\curso_python\entornos_virtuales\.venv\Lib\site-packages\pip (python 3.11)**

**(.ganadores)**
## PASO 10
para desactivar solo tenemos que colocar el siguiente comando

**deactivate**

## PASO 11
para volver a activar colocamos el comando  `source .(nombre de la carpeta creada)/scripts/activate`

**source .ganadores/scripts/activate**








