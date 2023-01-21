from entidades.parking import Parking
from entidades.plaza import Plaza
from entidades.vehiculo import Vehiculo
from entidades.abonado import Abonado


if __name__ == "__main__":
    #EL PIN Y LOS ID PASARLOS A INT
    parking = Parking(12) 

    car1 = Vehiculo("6230GVD", "car")
    moto1 = Vehiculo("3030TSS2", "motorcycle")
    minus = Vehiculo("7777", "handicapped")

    cocheabonado = Vehiculo("0000", "handicapped")


    abonado1 = Abonado("53771267L","Nicolás","Bursón","77777","mensual","nicoffb@hotmail.com",car1)

    
    print("Plazas disponibles iniciales:", parking.calcular_plazas_libres()) 

    plaza1 = Plaza(1, car1, abonado1)
    parking.addPlaza(plaza1)

    plaza2 = Plaza(2, moto1, None)
    parking.addPlaza(plaza2)
  
    plaza3 = Plaza(3, minus, None)
    parking.addPlaza(plaza3)

    print("Plazas disponibles después de agregar 3 de ejemplo:", parking.calcular_plazas_libres())
    print(parking.plazas_disponibles_por_tipo())
    parking.imprimir_plazas()
    
    while True:
        print("--- Menú Principal ---")
        print("1. Acceso como Cliente")
        print("2. Acceso como Administrador")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Acceso como Cliente")
            while True:
                print("1. Depositar vehículo")
                print("2. Retirar vehículo")
                print("3. Depositar vehículo (ABONADO)")
                print("4. Retirar vehículo /ABONADO)")
                print("5. Salir")
                opcion = input("Ingresa tu opción: ")

                if opcion == "1":
                    print("Actualmente las plazas disponibles son: " , parking.plazas_disponibles_por_tipo())
                    print("Introduzca la matricula y el tipo de su vehículo")
                    matriculaD = input("Introduzca la matrícula del vehículo: ")
                    tipo = input("Introduzca el tipo de vehículo (car, motorcycle, handicapped): ")
                    parking.depositar_vehiculo(matriculaD,tipo)
                    #parking.imprimir_plazas()   comprobacion de que se actualizan y se pone ocupadas

                elif opcion == "2":
                    print("Introduzca su matrícula, el identificador2 de la plaza y el pin del ticket")
                    matriculaR = input("Introduzca la matrícula del vehículo: ")
                    idR = int(input("Introduzca el identificador"))
                    pinR = int(input("Introduzca el pin"))
                    parking.retirarVehiculo(matriculaR,idR,pinR)
                    parking.plazas_disponibles_por_tipo()
                    parking.imprimir_plazas()
                
                elif opcion == "3": 
                    matriculaC = input("Introduzca la matrícula del vehículo: ")
                    dniC = input("Introduzca su DNI: ")
                    parking.depositar_abonados(matriculaC,dniC)
                
                elif opcion == "4":
                    matriculaT = input("Introduzca la matrícula del vehículo: ")
                    idT = int(input("Introduzca el identificador"))
                    pinT = int(input("Introduzca el pin"))

                       
                elif opcion == "5":
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida")


        elif opcion == "2":
            print("Acceso como Administrador")
            while True:
                print("1. Estado del parking")
                print("2. Facturación")
                print("3. Alta abonado")
                print("4. Baja abonado")
                print("5. Salir")
                opcion = input("Ingresa tu opción: ")

                if opcion == "1":
                    parking.calcular_plazas_libres()
                    parking.plazas_disponibles_por_tipo()
                    parking.imprimir_plazas_con_abonados()
                elif opcion == "2":
                    parking.facturacion.__str__()
                elif opcion == "3":
                    parking.solicitar_datos_abonado()
                elif opcion == "4":
                    dniZ = input("Introduzca el DNI: ")
                    parking.baja_abonado(dniZ)
                elif opcion == "5":
                    break
                else:
                    print("Opción no válida")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor selecciona una opción válida.")

    















   

