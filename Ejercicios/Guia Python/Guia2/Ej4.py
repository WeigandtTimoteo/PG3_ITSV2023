class Operaciones:
    def __init__(self):
        global num1, num2
        num1 = input("Ingrese el primer numero entero: ")
        num2 = input("Ingrese el segundo numero entero: ")
        self.suma(num1, num2)
        self.resta(num1, num2)
        self.multiplicacion(num1, num2)
        self.division(num1, num2)
    
    def suma(self, num1, num2):
        print("La suma es: ", int(num1) + int(num2))

    def resta(self, num1, num2):
        print("La resta es: ", int(num1) - int(num2))
    
    def multiplicacion(self, num1, num2):
        print("La multiplicacion es: ", int(num1) * int(num2))

    def division(self, num1, num2):
        print("La division es: ", int(num1) / int(num2))

nums1 = Operaciones()