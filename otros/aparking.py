class Parking:
    def __init__(self, capacity):
        self.capacity_types = {"car": round(capacity*0.7), "motorcycle": round(capacity*0.15), "handicapped": round(capacity*0.15)}
        self.tiposdeplaza_ocupadas = {"car": 0, "motorcycle": 0, "handicapped": 0}
        self.plazas_ocupadas = {}

    def asignar_plaza(self, matricula, tipo_vehiculo):
        if tipo_vehiculo in self.capacity_types:
            if self.capacity_types[tipo_vehiculo] > self.tiposdeplaza_ocupadas[tipo_vehiculo]:
                self.plazas_ocupadas[matricula] = tipo_vehiculo
                self.tiposdeplaza_ocupadas[tipo_vehiculo] += 1
                return f"Se ha asignado una plaza de {tipo_vehiculo} a la matrícula {matricula}."
            else:
                return f"Lo siento, no hay plazas de {tipo_vehiculo} disponibles en este momento."
        else:
            return "Tipo de vehículo no válido. Por favor, introduzca 'car', 'motorcycle' o 'handicapped'."