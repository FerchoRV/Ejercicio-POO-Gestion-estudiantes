from estudiante import Estudiante
from asignatura import Asignatura
from SistemaGestionEstudiantes import SistemaGestionEstudiantes

#Ejemplo de uso:
sistema = SistemaGestionEstudiantes()

# Crear estudiantes
estudiante1 = Estudiante("Juan","Pérez", 20)
estudiante2 = Estudiante("María","Gómez", 22)

# Crear asignaturas
asignatura1 = Asignatura("Matemáticas")
asignatura2 = Asignatura("Ciencias")

# Agregar estudiantes y asignaturas al sistema
sistema.agregar_estudiante(estudiante1)
sistema.agregar_estudiante(estudiante2)
sistema.agregar_asignatura(asignatura1)
sistema.agregar_asignatura(asignatura2)

# Asignar notas
sistema.asignar_nota(estudiante1, asignatura1, 90)
sistema.asignar_nota(estudiante1, asignatura2, 85)
sistema.asignar_nota(estudiante2, asignatura1, 88)
sistema.asignar_nota(estudiante2, asignatura2, 92)

# Mostrar notas y promedios
sistema.mostrar_notas_estudiante(estudiante1)
sistema.mostrar_notas_estudiante(estudiante2)
sistema.promedio_general_estudiante(estudiante1)
sistema.promedio_general_estudiante(estudiante2)
sistema.promedio_asignatura(asignatura1)
sistema.promedio_asignatura(asignatura2)

