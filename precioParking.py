class PrecioParking:
    def __init__(self, capacity):
        self.capacity = capacity
        self.plaza = []
        self.pricing = {"car": 0.12, "motorcycle": 0.08, "handicapped": 0.10}
        self.capacity_types = {"car": round(capacity*0.7), "motorcycle": round(capacity*0.15), "handicapped": round(capacity*0.15)}
        self.occupied_types = {"car": 0, "motorcycle": 0, "handicapped": 0}
        self.plazas_ocupadas = {}

    def add_plaza(self, plaza, type_car):
        if self.capacity_types[type_car] > self.occupied_types[type_car]:
            self.occupied_types[type_car] += 1
            self.plaza.append({"plaza": plaza, "type": type_car})
            print(f'Añadido {plaza} of type {type_car}. Espacios restantes: {self.get_free_spaces()}')
            return True
        else:
            print(f'No more space for {type_car}s. Espacios restantes: {self.get_free_spaces()}')
            return False

    def remove_plaza(self, plaza):
        for parked_car in self.plaza:
            if parked_car["plaza"] == plaza:
                self.occupied_types[parked_car["type"]] -= 1
                self.plaza.remove(parked_car)
                print(f'Eliminado {plaza}. Espacios restantes: {self.get_free_spaces()}')
                return True
        print(f'{plaza} not found in parking.')
        return False

    def get_free_spaces(self):
        free_spaces = {"car": self.capacity_types["car"] - self.occupied_types["car"],
                       "motorcycle": self.capacity_types["motorcycle"] - self.occupied_types["motorcycle"],
                       "handicapped": self.capacity_types["handicapped"] - self.occupied_types["handicapped"]}
        return free_spaces

    def get_pricing(self, car_type, minutes):
        return self.pricing[car_type] * minutes
    
   
    # def asignar_plaza(self, matricula, tipo_vehiculo):
    #     if tipo_vehiculo == "turismo":
    #         if self.capacity_types[tipo_vehiculo] > 0:
    #             self.plazas_ocupadas[matricula] = tipo_vehiculo
    #             self.occupied_types[tipo_vehiculo] += 1
    #             return f"Se ha asignado una plaza de turismo a la matrícula {matricula}."
    #         else:
    #             return "Lo siento, no hay plazas de turismo disponibles en este momento."
    #     elif tipo_vehiculo == "motocicleta":
    #         if self.num_plazas_motocicleta > 0:
    #             self.plazas_ocupadas[matricula] = tipo_vehiculo
    #             self.num_plazas_motocicleta -= 1
    #             return f"Se ha asignado una plaza de motocicleta a la matrícula {matricula}."
    #         else:
    #             return "Lo siento, no hay plazas de motocicleta disponibles en este momento."
    #     elif tipo_vehiculo == "movilidad reducida":
    #         if self.num_plazas_movilidad_reducida > 0:
    #             self.plazas_ocupadas[matricula] = tipo_vehiculo
    #             self.num_plazas_movilidad_reducida -= 1
    #             return f"Se ha asignado una plaza de movilidad reducida a la matrícula {matricula}."
    #         else:
    #             return "Lo siento, no hay plazas de movilidad reducida disponibles en este momento."
    #     else:
    #         return "Tipo de vehículo no válido. Por favor, introduzca 'turismo', 'motocicleta' o 'movilidad reducida'."