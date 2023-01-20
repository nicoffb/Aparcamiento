from precioParking import PrecioParking
    # Crear una instancia de la clase Parking
if __name__ == "__main__":
    parking = PrecioParking(100)

    print(parking.get_free_spaces()) 

    plaza1 = "Plaza 1"
    plaza2 = "Plaza 2"
    plaza3 = "Plaza 3"
    plaza4 = "Plaza 4"

    print("--------------------------------------------------")

    # adding cars
    print(parking.add_plaza(plaza1, "car")) # True
    print(parking.add_plaza(plaza2, "car")) # True
    print(parking.add_plaza(plaza3, "motorcycle")) # True
    print(parking.add_plaza(plaza4, "handicapped")) # True

    # trying to add a car to a full spot
    print(parking.add_plaza("Plaza 5", "car")) # False

    # removing a car
    print(parking.remove_plaza(plaza1)) # True

    # getting free spaces
    print(parking.get_free_spaces()) # {"car": 67, "motorcycle": 14, "handicapped": 14}

    # getting pricing for parking for 10 minutes
    print(parking.get_pricing("car", 10)) # 1.2
    print(parking.get_pricing("motorcycle", 10)) # 0.8
    print(parking.get_pricing("handicapped", 10)) # 1.0