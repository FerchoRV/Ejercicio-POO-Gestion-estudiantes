class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = {}

    def agregar_nota(self, asignatura, nota):
        self.notas[asignatura] = nota

    def promedio_general(self):
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} (Edad: {self.edad})"
