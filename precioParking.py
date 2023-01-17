class PrecioParking:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []
        self.pricing = {"car": 0.12, "motorcycle": 0.08, "handicapped": 0.10}
        self.capacity_types = {"car": round(capacity*0.7), "motorcycle": round(capacity*0.15), "handicapped": round(capacity*0.15)}
        self.occupied_types = {"car": 0, "motorcycle": 0, "handicapped": 0}

    def add_car(self, car, type_car):
        if self.capacity_types[type_car] > self.occupied_types[type_car]:
            self.occupied_types[type_car] += 1
            self.cars.append({"car": car, "type": type_car})
            print(f'Añadido {car} of type {type_car}. Espacios restantes: {self.get_free_spaces()}')
            return True
        else:
            print(f'No more space for {type_car}s. Espacios restantes: {self.get_free_spaces()}')
            return False

    def remove_car(self, car):
        for parked_car in self.cars:
            if parked_car["car"] == car:
                self.occupied_types[parked_car["type"]] -= 1
                self.cars.remove(parked_car)
                print(f'Eliminado {car}. Espacios restantes: {self.get_free_spaces()}')
                return True
        print(f'{car} not found in parking.')
        return False

    def get_free_spaces(self):
        free_spaces = {"car": self.capacity_types["car"] - self.occupied_types["car"],
                       "motorcycle": self.capacity_types["motorcycle"] - self.occupied_types["motorcycle"],
                       "handicapped": self.capacity_types["handicapped"] - self.occupied_types["handicapped"]}
        return free_spaces

    def get_pricing(self, car_type, minutes):
        return self.pricing[car_type] * minutes
