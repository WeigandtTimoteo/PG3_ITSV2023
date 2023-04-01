class Triangulo:
    def lados(self):
        global lado1, lado2, lado3
        lado1 = int(input("Ingrese el lado 1: "))
        lado2 = int(input("Ingrese el lado 2: "))
        lado3 = int(input("Ingrese el lado 3: "))

    def mayor(self):
        if lado1 > lado2 and lado1 > lado3:
            print("El mayor es el lado 1, con un valor de: ", lado1)
        elif lado2 > lado1 and lado2 > lado3:
            print("El mayor es el lado 2, con un valor de: ", lado2)
        elif lado3 > lado1 and lado3 > lado2:
            print("El mayor es el lado 3, con un valor de: ", lado3)
    
    def equilatero(self):
        if lado1 == lado2 and lado1 == lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")

triangulo = Triangulo()
triangulo.lados()
triangulo.mayor()
triangulo.equilatero()