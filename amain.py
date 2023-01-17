from aaparking import Parking

if __name__ == "__main__":
    parking = Parking(100)
    print(parking.get_free_spaces())
    matricula = input("Introduce la matrícula del vehículo: ")
    tipo_vehiculo = input("Introduce el tipo de vehículo (car, motorcycle o handicapped): ")
    resultado = parking.asignar_plaza(matricula, tipo_vehiculo)
    print(resultado)
    print(parking.get_free_spaces())
    
    
    matricula2 = input("Introduce la matrícula del vehículo: ")
    plaza = int(input("Introduce la plaza asignada "))
    pin = int(input("Introduce el pin asignado "))
    parking.calcular_coste(matricula2,plaza,pin)
    print(parking.get_free_spaces())
    # por qué me da datos no validos