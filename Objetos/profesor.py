##########################
##
##  ACA VA LA CLASE
##
##########################

class Profesor:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

profesor_pepe:Profesor = Profesor("Pepe", "jose@um.edu.ar")
print(id(profesor_pepe))
print("el nombre es: ")
print(profesor_pepe.nombre)
print("el email es: ")
print(profesor_pepe.email)
print("su asistencia es: ")
print(profesor_pepe.asistencia)

print("EL PROFESOR FUE A CLASE...")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("su asistencia es: ")
print(profesor_pepe.asistencia)

profesor_pepe.cambiar_nombre("JOSE!")

print(profesor_pepe.nombre)


profesor_walter = Profesor("Walter")
profesor_daniel = Profesor("Daniel")

print(id(profesor_daniel))
print(profesor_daniel.nombre)
print(profesor_daniel.nombre)
print(id(profesor_walter))
print(profesor_walter.nombre)

class alumno:
    def __init__(self, param_nombre, param_email, param_telefono, numero_alumno):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0
        self.telefono = param_telefono 
        self.numero_alumno = numero_alumno

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def cambiar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono   

    def asistencia_clase(self):
        self.asistencia += 1
            
alumno_facundo:alumno = alumno("Facundo", "f.mangione@alumno.um.ed.ar", "2612461975", 62158)
print(id(alumno_facundo))
print("el nombre es: ")
print(alumno_facundo.nombre)
print("el email es: ")
print(alumno_facundo.email)
print("su asistencia es: ")
print(alumno_facundo.asistencia)   
print("su numero de telefono es: ")  
print(alumno_facundo.telefono)   
print("su legajo es ")
print(alumno_facundo.numero_alumno)

print("El alumno fue a clase...")
alumno_facundo.asistencia_clase()
alumno_facundo.asistencia_clase()
alumno_facundo.asistencia_clase()
alumno_facundo.asistencia_clase()
alumno_facundo.asistencia_clase()
alumno_facundo.asistencia_clase()
alumno_facundo.asistencia_clase()

print("su asistencia es: ")
print(alumno_facundo.asistencia)