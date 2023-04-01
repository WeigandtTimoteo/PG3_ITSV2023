class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cargar(self):
        self.nombre = input("Ingrese nombre: ")
        self.edad = int(input("Ingrese edad: "))

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            return("El empleado paga impuestos")
        else:
            return("El empleado no paga impuestos")

    def cargar(self):
        super().cargar()
        self.sueldo = float(input("Ingrese sueldo: "))

    def imprimir(self):
        super().imprimir()
        print(f"Sueldo: {self.sueldo}, {self.pagar_impuestos()}")

pepe = Persona("Pepe", 25)
pepe.imprimir()
pepe.cargar()
pepe.imprimir()

alejandro = Empleado("Alejandro", 30, 4000)
alejandro.imprimir()
alejandro.cargar()
alejandro.imprimir()
