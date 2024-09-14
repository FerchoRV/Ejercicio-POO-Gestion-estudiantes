from Estudiante import Estudiante
from Materia import Materia
from OperacionesSistema import OperacionesSistema

sistema = OperacionesSistema()

# Crear materias
materia1 = Materia('Matematicas', 10)
materia2 = Materia('Ingles', 5)
materia3 = Materia('Quimica', 15)

sistema.crear_materia(materia1.nombre, materia1.capacidad)
sistema.crear_materia(materia2.nombre, materia2.capacidad)
sistema.crear_materia(materia3.nombre, materia3.capacidad)

# Crear estudiantes
estudiante1 = Estudiante(100, 'Juan', 'Perez', 20)
estudiante2 = Estudiante(101, 'Pedro', 'Guzman', 30)
estudiante3 = Estudiante(102, 'Andrea', 'Chavez', 25)
estudiante4 = Estudiante(103, 'Maria', 'Lopez', 22)
estudiante5 = Estudiante(104, 'Luis', 'Martinez', 24)
estudiante6 = Estudiante(105, 'Ana', 'Fernandez', 21)
estudiante7 = Estudiante(106, 'Jorge', 'Morales', 23)
estudiante8 = Estudiante(107, 'Paula', 'Cordero', 26)
estudiante9 = Estudiante(108, 'Sofia', 'Ramirez', 27)
estudiante10 = Estudiante(109, 'Carlos', 'Gonzalez', 28)
estudiante11 = Estudiante(110, 'Natalia', 'Torres', 29)
estudiante12 = Estudiante(111, 'Felipe', 'Rodriguez', 20)
estudiante13 = Estudiante(112, 'Juliana', 'Vasquez', 21)
estudiante14 = Estudiante(113, 'Santiago', 'Suarez', 22)
estudiante15 = Estudiante(114, 'Valeria', 'Salazar', 23)

# Crear estudiantes en el sistema
for estudiante in [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, estudiante6, estudiante7, estudiante8, estudiante9, estudiante10, estudiante11, estudiante12, estudiante13, estudiante14, estudiante15]:
    sistema.crear_estudiante(estudiante.id, estudiante.nombre, estudiante.apellido, estudiante.edad)

# Vincular estudiantes con materias
for estudiante_id in [100, 101, 102, 103, 104]:
    sistema.vincular_estudiante_materia('Matematicas', estudiante_id)

for estudiante_id in [105, 106, 107, 108, 109]:
    sistema.vincular_estudiante_materia('Ingles', estudiante_id)

for estudiante_id in [110, 111, 112, 113, 114]:
    sistema.vincular_estudiante_materia('Quimica', estudiante_id)

# Agregar notas
sistema.agregar_notas('Matematicas', 100, 8)
sistema.agregar_notas('Matematicas', 101, 9)
sistema.agregar_notas('Ingles', 105, 80)
sistema.agregar_notas('Ingles', 106, 85)
sistema.agregar_notas('Quimica', 110, 90)
sistema.agregar_notas('Quimica', 111, 92)

# Consultas
print("Notas del estudiante con ID 100:")
sistema.mostrar_notas_y_promedio(100, 'Matematicas')

print("\nNotas y promedio en todas las materias del estudiante con ID 100:")
sistema.mostrar_notas_y_promedios_todas_materias(100)

print("\nLista de estudiantes en la materia 'Matematicas':")
print(sistema.obtener_estudiantes_completos_por_materia('Matematicas'))

print("\nMaterias a las que está asociado el estudiante con ID 100:")
print(sistema.obtener_materias_por_estudiante(100))





