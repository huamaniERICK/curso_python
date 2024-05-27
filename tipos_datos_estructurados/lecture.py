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