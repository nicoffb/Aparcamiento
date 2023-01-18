
from entidades.aaparking import Parking
from entidades.plaza import Plaza
from entidades.vehiculo import Vehiculo


# if __name__ == "__main__":
#     # Crear un objeto Parking
#     estacionamiento = Parking(100)

#     # Crear algunos objetos de vehículo
#     carro1 = Vehiculo("carro", "ABC123")
#     carro2 = Vehiculo("carro", "DEF456")
#     moto1 = Vehiculo("moto", "GHI789")
#     moto2 = Vehiculo("moto", "JKL012")
#     discapacitado = Vehiculo("disc","6780GTS")

#     # Crear algunos objetos de plaza y asignarles un vehículo
#     plaza1 = Plaza(carro1, "Juan", "1234")
#     plaza2 = Plaza(carro2, "Maria", "5678")
#     plaza3 = Plaza(moto1, "Pedro", "9101")
#     plaza4 = Plaza(moto2, "Sofia", "1213")

#     # Añadir las plazas al estacionamiento
#     estacionamiento.addPlaza(plaza1)
#     estacionamiento.addPlaza(plaza2)
#     estacionamiento.addPlaza(plaza3)
#     estacionamiento.addPlaza(plaza4)

#     # Imprimir las plazas libres por tipo
#     plazasLibres = estacionamiento.plazasLibresPorTipo()
#     for tipo, cantidad in plazasLibres.items():
#         print(f"Plazas libres de tipo {tipo}: {cantidad}")

if __name__ == "__main__":
    # Crear un objeto Parking con 100 plazas
    estacionamiento = Parking(100)

    # Imprimir las plazas libres por tipo
    plazasLibres = estacionamiento.plazasLibresPorTipo()
    for tipo, cantidad in plazasLibres.items():
        print(f"Plazas libres de {tipo}: {cantidad}")

    # Crear una plaza
    vehiculo = Vehiculo("car", "ABC123")
    cliente = "Juan Perez"
    pin = 1234
    plaza = Plaza(vehiculo, cliente, pin)

    # Añadir la plaza al estacionamiento
    estacionamiento.addPlaza(plaza)

    # Imprimir las plazas libres por tipo
    plazasLibres = estacionamiento.plazasLibresPorTipo()
    for tipo, cantidad in plazasLibres.items():
        print(f"Plazas libres de {tipo}: {cantidad}")