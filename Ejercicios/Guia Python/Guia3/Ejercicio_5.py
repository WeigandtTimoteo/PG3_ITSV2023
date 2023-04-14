try:
    with open("Ejercicio_5.txt","a") as file:
        file.write(int(2345))

except TypeError:
    print("Ingrese un String, no un numero")

finally:
    None