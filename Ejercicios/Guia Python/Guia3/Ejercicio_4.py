while True:
    try:
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        print("El resultado de la division es: ", n1 / n2)

    except ZeroDivisionError:
        print("No se puede dividir por cero")

    except ValueError:
        print("Ingrese un numero valido")

    finally:
        print("Fin de la operación")