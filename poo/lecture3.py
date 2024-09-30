# crear una lista de alumnos con los atributos que usted crea por comveniente
# luego instanciara a 4 alumnos
class alumno:
    def __init__(self,nombre,apellidos,edad,dni,genero="masculino"):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        self.dni=dni
        self.genero=genero

    # metodos
    def escribir(self):
        print("estoy escribiendo")
    
    def tarea(self,nombre_docente):
        print("haciendo la tarea de:",nombre_docente)
    
    def terminar_tarea(self):
        print(" terminando tarea anterior")


perci=alumno("perci","yarihuaman mitma",22,63748263,)
print(perci.genero)

# bretmer=alumno("bretmer","condori huamantoma",19,74532984,)
# print(bretmer.mostrar_alumno())

ruth=alumno("ruth","castillo huamani",18,64738294,"femenino")


erick=alumno("erick","huamani ccahuay",20,71331386,)

erick.tarea("jhon")