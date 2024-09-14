class OperacionesSistema:
    def __init__(self):
        self.estudiantes = {}
        self.materias = {}
        self.datos = {}
        self.notas = {}

    def crear_materia(self, nombre, capacidad):
        if nombre not in self.materias:
            self.materias[nombre] = {"Estado": True, "Capacidad": capacidad}
        else:
            print("La materia ya esta registrada en el sistema")

    def actualizar_materia(self, nombre_antiguo, nombre_nuevo, capacidad=None):
        if nombre_antiguo in self.materias:            
            materia_info = self.materias.pop(nombre_antiguo)     

                        
            if capacidad is not None:
                materia_info["Capacidad"] = capacidad

                        
            self.materias[nombre_nuevo] = materia_info
            
            if nombre_antiguo in self.datos:
                self.datos[nombre_nuevo] = self.datos.pop(nombre_antiguo)
            
            
            for estudiante_id in self.notas:
                if nombre_antiguo in self.notas[estudiante_id]:
                    self.notas[estudiante_id][nombre_nuevo] = self.notas[estudiante_id].pop(nombre_antiguo)
            print(f"Materia actualizada: {nombre_nuevo}")
        else:
            print(f"La materia {nombre_antiguo} no existe.")


    def eliminar_materia(self, nombre):
        if nombre in self.materias:
        
            del self.materias[nombre]
        
        
            if nombre in self.datos:
                del self.datos[nombre]
        
        
            for id_estudiante, materias in self.notas.items():
                if nombre in materias:
                    del materias[nombre]

            print(f"Materia '{nombre}' eliminada correctamente.")
        else:
            print("Materia no encontrada")


    def crear_estudiante(self, id, nombre, apellido, edad):
        if id not in self.estudiantes:
            self.estudiantes[id] = {"Nombre": nombre, "Apellido": apellido, "Edad": edad}
        else:
            print("El estudiante ya esta registrado en el sistema")

    def actualizar_datos_estudiante(self, id, nombre=None, apellido=None, edad=None):
        if id in self.estudiantes:
            if nombre is not None:
                self.estudiantes[id]["Nombre"] = nombre
            if apellido is not None:
                self.estudiantes[id]["Apellido"] = apellido
            if edad is not None:
                self.estudiantes[id]["Edad"] = edad
        else:
            print("Estudiante no encontrado")

    def actualizar_id_estudiante(self, id_viejo, id_nuevo):
        if id_viejo in self.estudiantes:
        
            self.estudiantes[id_nuevo] = self.estudiantes.pop(id_viejo)        
        
            for materia, lista_estudiantes in self.datos.items():
                if id_viejo in lista_estudiantes:
                    lista_estudiantes[lista_estudiantes.index(id_viejo)] = id_nuevo
        
            if id_viejo in self.notas:
                self.notas[id_nuevo] = self.notas.pop(id_viejo)
        
            print(f"ID del estudiante actualizado de {id_viejo} a {id_nuevo}")
        else:
            print("Estudiante no encontrado")

    def eliminar_estudiante(self, id):
        if id in self.estudiantes:
        
            del self.estudiantes[id]

        
            for materia, lista_estudiantes in self.datos.items():
                if id in lista_estudiantes:
                    lista_estudiantes.remove(id)
        
        
            if id in self.notas:
                del self.notas[id]
        
            print(f"Estudiante con ID {id} eliminado correctamente.")
        else:
            print("Estudiante no encontrado")     



    def vincular_estudiante_materia(self, materia, id):
        if materia in self.materias:
            if self.materias[materia]["Capacidad"] > 0:
                if id in self.estudiantes:
                    
                    if materia not in self.datos:
                        self.datos[materia] = []
                    
                    self.datos[materia].append(id)
                    self.materias[materia]["Capacidad"] -= 1
                else:
                    print("Estudiante no registrado en el sistema")
            else:
                print("Cupo lleno, no puede agregar más estudiantes a esta materia")
        else:
            print("Materia no registrada en el sistema")

    def agregar_notas(self, materia, id, nota):
        if materia in self.datos and id in self.datos[materia]:
            
            if id not in self.notas:
                self.notas[id] = {}
            if materia not in self.notas[id]:
                self.notas[id][materia] = []
            
            self.notas[id][materia].append(nota)
        else:
            print("Estudiante sin registrar en la materia")

    def actualizar_nota(self, id_estudiante, materia, nueva_nota, index_nota):
        if id_estudiante in self.notas:
            if materia in self.notas[id_estudiante]:
                if 0 <= index_nota < len(self.notas[id_estudiante][materia]):
                
                    self.notas[id_estudiante][materia][index_nota] = nueva_nota
                    print(f"Nota actualizada correctamente en la materia '{materia}' para el estudiante con ID {id_estudiante}.")
                else:
                    print("Índice de nota no válido.")
            else:
                print(f"Materia '{materia}' no registrada para el estudiante con ID {id_estudiante}.")
        else:
            print(f"Estudiante con ID {id_estudiante} no encontrado.")
            
    def consultar_notas_estudiante(self, id_estudiante):
        if id_estudiante in self.notas:
            return self.notas[id_estudiante]
        else:
            print("Estudiante no encontrado")
            return {}
        
    def promedio_notas_estudiante(self, id_estudiante):
        if id_estudiante in self.notas:
            notas = [nota for materia in self.notas[id_estudiante].values() for nota in materia]
            if notas:
                return sum(notas) / len(notas)
            else:
                return 0
        else:
            print("Estudiante no encontrado")
            return 0
        
    def mostrar_notas_y_promedio(self, id_estudiante, materia):
        if id_estudiante in self.notas:
            if materia in self.notas[id_estudiante]:
                notas = self.notas[id_estudiante][materia]
                if notas:
                    promedio = sum(notas) / len(notas)
                    print(f"Notas del estudiante con ID {id_estudiante} en la materia '{materia}': {notas}")
                    print(f"Promedio de notas en la materia '{materia}': {promedio:.2f}")
                else:
                    print(f"No hay notas registradas para el estudiante con ID {id_estudiante} en la materia '{materia}'.")
            else:
                print(f"El estudiante con ID {id_estudiante} no está registrado en la materia '{materia}'.")
        else:
            print(f"Estudiante con ID {id_estudiante} no encontrado.")

    def mostrar_notas_y_promedios_todas_materias(self, id_estudiante):
        if id_estudiante in self.notas:
            todas_notas = self.notas[id_estudiante]
        
            if todas_notas:
                for materia, notas in todas_notas.items():
                    if notas:
                        promedio = sum(notas) / len(notas)
                        print(f"Notas del estudiante con ID {id_estudiante} en la materia '{materia}': {notas}")
                        print(f"Promedio de notas en la materia '{materia}': {promedio:.2f}")
                    else:
                        print(f"No hay notas registradas para el estudiante con ID {id_estudiante} en la materia '{materia}'.")
            else:
                print(f"No hay materias registradas para el estudiante con ID {id_estudiante}.")
        else:
            print(f"Estudiante con ID {id_estudiante} no encontrado.")

    def obtener_estudiantes_completos_por_materia(self, materia):
        estudiantes_materia = []
        if materia in self.datos:
            for id_estudiante in self.datos[materia]:
                info_estudiante = self.estudiantes.get(id_estudiante, {})
                if info_estudiante:
                    estudiantes_materia.append({
                        'ID': id_estudiante,
                        'Nombre': info_estudiante.get('Nombre'),
                        'Apellido': info_estudiante.get('Apellido'),
                        'Edad': info_estudiante.get('Edad')
                    })
        return estudiantes_materia

    
    def obtener_materias_por_estudiante(self, id_estudiante):
        materias = []
        for materia, lista_estudiantes in self.datos.items():
            if id_estudiante in lista_estudiantes:
                materias.append(materia)
        return materias
    






       