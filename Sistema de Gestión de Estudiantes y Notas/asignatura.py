class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = {}

    def agregar_estudiante(self, estudiante, nota):
        self.estudiantes[estudiante] = nota

    def promedio_asignatura(self):
        if not self.estudiantes:
            return 0
        return sum(self.estudiantes.values()) / len(self.estudiantes)
    
    def __str__(self):
        return self.nombre