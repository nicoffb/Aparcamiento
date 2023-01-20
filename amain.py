from entidades.aaparking import Parking
from entidades.plaza import Plaza
from entidades.vehiculo import Vehiculo
from entidades.abonado import Abonado


if __name__ == "__main__":

    parking = Parking(12) 

    car1 = Vehiculo("6230GVD", "car")
    moto1 = Vehiculo("3030TSS", "motorcycle")
    minus = Vehiculo("7777", "handicapped")


    abonado1 = Abonado("53771267L","Nicolás","Bursón","77777","Mensual","nicoffb@hotmail.com",car1)
    print(abonado1.str())
    
    print("Plazas disponibles:", parking.calcular_plazas_libres()) 

    plaza1 = Plaza(1, car1, abonado1)
    parking.addPlaza(plaza1)

    plaza2 = Plaza(2, moto1, None)
    parking.addPlaza(plaza2)
  
    plaza3 = Plaza(3, minus, None)
    parking.addPlaza(plaza3)

    


    print("Plazas disponibles:", parking.calcular_plazas_libres())
    print(parking.plazas_disponibles_por_tipo())

    parking.depositar_abonados(plaza1.vehiculo.matricula,plaza1.abonado.dni)

    
    matricula = input("Introduce la matrícula del vehículo: ")
    dni = input("Introduce tu dni")



    parking.depositar_abonados(matricula,dni)


















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
    

