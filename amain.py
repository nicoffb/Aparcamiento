from entidades.aaparking import Parking
from entidades.plaza import Plaza
from entidades.vehiculo import Vehiculo


if __name__ == "__main__":
    parking = Parking(100)

    car1 = Vehiculo("123ABC", "car")
    car2 = Vehiculo("456DEF", "car")
    motorcycle1 = Vehiculo("789GHI", "motorcycle")
    handicapped1 = Vehiculo("101JKL", "handicapped")

    plazaCoche = Plaza(1,car1)

    parking.addPlaza(plazaCoche)

    print(parking.plazasLibres())
   
    

