while True:
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    try:
        mes = int(input("Ingrese el numero del mes: "))
        if mes <= 0:
            print("Ingrese un numero del 1 al 12")
        else:
            print(meses[mes-1])
    except IndexError:
        print("Ingrese un numero del 1 al 12")