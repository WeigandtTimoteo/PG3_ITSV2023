while True:
        try:
            n1 = int(input("Ingrese el primer número: "))
            n2 = int(input("Ingrese el segundo número: "))
            print("El resultado de la suma es: ", n1 + n2)
        except ValueError:
            print("Ingrese un número")
        finally:
            val = input("Desea seguir ejecutando el programa? (s/n)")
            if val == "n":
                print("Fin del programa")
                break