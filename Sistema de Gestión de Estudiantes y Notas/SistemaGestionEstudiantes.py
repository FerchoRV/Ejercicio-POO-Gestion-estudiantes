class SistemaGestionEstudiantes:
    def __init__(self):
        self.estudiantes = {}
        self.asignaturas = {}

    def agregar_estudiante(self, estudiante):
        self.estudiantes[estudiante] = True

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            del self.estudiantes[estudiante]

    def agregar_asignatura(self, asignatura):
        self.asignaturas[asignatura] = True

    def eliminar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            del self.asignaturas[asignatura]

    def asignar_nota(self, estudiante, asignatura, nota):
        if estudiante in self.estudiantes and asignatura in self.asignaturas:
            asignatura.agregar_estudiante(estudiante, nota)
            estudiante.agregar_nota(asignatura, nota)

    def mostrar_notas_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            print(f"Notas de {estudiante}:")
        for asignatura, nota in estudiante.notas.items():
            print(f"{asignatura}: {nota}")

    def promedio_general_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            print(f"Promedio de {estudiante}: {estudiante.promedio_general()}")
            
    def promedio_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            print(f"Promedio de {asignatura}: {asignatura.promedio_asignatura()}")