# # crear una lista de 5 alumnos cada alumno almacenaremos su nombre,apellidos y edad
# lista_alumnos=[{
#     "nombre":"william",
#     "apellidos":"barrientos",
#     "edad":18,
# },{
#     "nombre":"erick",
#     "apellidos":"huamani",
#     "edad":20,
# },{
#     "nombre":"abel",
#     "apellidos":"llamocca",
#     "edad":25,
    
# },{
#     "nombre":"juan",
#     "apellidos":"lopez",
#     "edad":24,
    
# },{
#     "nombre":"daniel",
#     "apellidos":"huamani",
#     "edad":12,
# }

# ]
# # insertar al final los datos de antoni
# lista_nueva=[{
#     "nombres":"antoni",
#     "apellidos":"isase",
#     "edad":21,
# }]
# lista_alumnos.append(lista_nueva)
# print(lista_alumnos)

# # eliminar de la lista si existe los datos de abel



# # buscar y mostrar el alumno en la pocicion 4
# lista_alumnos=[{
#     "nombre":"abel",
#     "apellidos":"llamocca",
#     "edad":25,
# }
# ]
# indice=lista_alumnos.index[{
#     "nombre":"abel",
#     "apellidos":"llamocca",
#     "edad":25,
# }
# ]
# print(lista_alumnos[indice])


# # 2 crear una lista con 4 diccionarios donde tendran sus datos de sus mascotas(nombre,edad,sexo,raza)
# # tareas
# # mostrar la lista con los 4 diccionarios
# # editar el 3er registro y cambiarle la edad sin modificar la lista original
# # mostrar la lista original y luego la lista con el tercer registro modificado



mis_mascotas=[{
    "nombre":"guardian",
    "edad":7,
    "sexo":"macho",
    "raza":"bulldog",
},{
    "nombre":"peluza",
    "edad":4,
    "sexo":"hembra",
    "raza":"persa",
},{
    "nombre":"hueso",
    "edad":8,
    "sexo":"macho",
    "raza":"doberman",
},{
    "nombre":"pequeñin",
    "edad":6,
    "sexo":"hembra",
    "raza":"bengali",
}

]

print(mis_mascotas)

mis_mascotas[3]["edad"]=8
mis_mascotas[3]={"nombre":"pequeñin","edad":8,"sexo":"hembra","raza":"bengali"}
print(mis_mascotas)

copia_mascotas=mis_mascotas.copy()
print(mis_mascotas)
print(copia_mascotas)

# yo como dueño de mis mascotas
# deseo actualizar la edad de mis mascotas
# para tener una lista de correcta de mi mascota

# yo como dueño de mis mascotas
# deseo ver la lista original y la lista modificada
# para saber si se modifico correctamente los datos que agregue



# yo como estudiante del tecnologico 
# deseo ver  mi porcentaje de asistencias 
# para ver si estoy aprobado o desaprobado en el curso

