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
    

