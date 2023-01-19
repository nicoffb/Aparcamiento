from entidades.aaparking import Parking
from entidades.plaza import Plaza
from entidades.vehiculo import Vehiculo


if __name__ == "__main__":

    car1 = Vehiculo("6230GVD", "car")
    moto1 = Vehiculo("3030TSS", "motorcycle")
    minus = Vehiculo("7777", "handicapped")

    parking = Parking(100)  # Create a parking with 100 parking spaces
    plaza1 = Plaza(1, car1, None)
    parking.addPlaza(plaza1)

    plaza2 = Plaza(2, moto1, None)
    parking.addPlaza(plaza2)
  
    plaza3 = Plaza(3, minus, None)
    parking.addPlaza(plaza3)


    print("Plazas disponibles:", parking.calcular_plazas_libres())
    print(parking.plazas_disponibles_por_tipo())

    matricula = input("Introduce la matrícula del vehículo: ")
    tipo = input("Introduce el tipo de vehículo (car, motorcycle, handicapped): ")

    
    parking.asignar_plaza(matricula,tipo)

    # parking.removePlaza(plaza1)
    # parking.removePlaza(plaza3)

    print("VA A PROCEDER A SACAR EL VEHICULO")

    matricula2 = input("Introduce la matrícula del vehículo: ")
    id2 = int(input("Introduce el identificador "))
    pin = int(input("Introduce el pin"))

    parking.retirarVehiculo(matricula2,id2,pin)


    print(parking.plazas_disponibles_por_tipo())
    

