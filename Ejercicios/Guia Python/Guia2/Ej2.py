class Alumno:
    def alumno(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
        if self.nota >= 6:
            print("Aprobado")
        else:
            print("Reprobado")

pepe = Alumno()
pepe.alumno("Pepe", 5)
pepe.mostrar()

alejandro = Alumno()
alejandro.alumno("Alejandro", 7)
alejandro.mostrar()