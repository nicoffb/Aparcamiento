idPlaza = input("Introduce la plaza que quieres reservar: ")
dni3 = input("Introduce tu dni")
tipoA = input("¿De cuanto tiempo quieres el abono?")
parking.alta_abonado(idPlaza,dni3,tipoA)





    matricula = input("Introduce la matrícula del vehículo: ")
    tipo = input("Introduce el tipo de vehículo (car, motorcycle, handicapped): ")


    
    parking.asignar_plaza(matricula,tipo)
    
    #parking.imprimir_plazas()
    
    
    
    print("VA A PROCEDER A SACAR EL VEHICULO")

    matricula2 = input("Introduce la matrícula del vehículo: ")
    id = int(input("Introduce el id "))
    pin = int(input("Introduce el pin"))

    parking.retirarVehiculo(matricula2,id,pin)

    # parking.imprimir_plazas()

    # parking.calcularPago(tipo)
    