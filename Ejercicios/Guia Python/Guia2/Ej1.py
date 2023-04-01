class Persona:
    def nombre(self, nombre):
        self.nombre = nombre
    
    def printNombre(self):
        print("El nombre de la persona es: ", self.nombre)
    
pepe = Persona()
pepe.nombre("Pepe")
pepe.printNombre()

alejandro = Persona()
alejandro.nombre("Alejandro")
alejandro.printNombre()