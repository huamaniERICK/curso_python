lista=["abel","antoni","miguel"]
diccionario={"nombre":"antonio","edad":15, "sexo":False}
# metodos pra el trabajo con tipos de datos estructurado
print(diccionario["nombre"])
print(diccionario["edad"])

texto="hola"
lista_texto=list(texto)
lista2=[e for e in texto]

texto_largo="hola como estan bienvenidos al salon"
nuevo_texto=texto_largo[16:]
nueva_lista=nuevo_texto.split(" ")
print(nueva_lista)


texto_largo="la vida es el arte de, dibujar sin borrar"
nuevo_texto=texto_largo.split(" ")
print(",".join(nuevo_texto))


lista["hola"]
lista.append("mundo")
print(lista)


# dato primitivo
nombre="abel"
otro_nombre=nombre
print(id(nombre))
print(id(otro_nombre))

# dato estructurado
lista_original=[1,2,3,4]
copia_lista=lista_original
lista_original[-1]=15
print(copia_lista)

# crear un programa que reciba una lista desordenada y muestre por terminal una lista ordenada y la lista previa a ser ordenada.
lista=[1,4,2,6,3]
copia_lista=lista.copy()
copia_lista.sort()
print(lista)
print(copia_lista)


alumnos=[{
    "nombre":"abel",
    "edad":15,
},{
    "nombre":"antoni",
    "edad":29,
}
]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por definir"
print(alumnos)
