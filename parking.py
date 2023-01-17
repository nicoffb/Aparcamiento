class Parking:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.plazas = []

    def add_car(self, car):
        if len(self.plazas) < self.capacity:
            self.plazas.append(car)
            return True
        return False
        
    def remove_car(self, car):
        if car in self.plazas:
            self.plazas.remove(car)
            return True
        return "No se ha encontrado el coche seleccionado"
    
    def is_full(self):
        return len(self.plazas) == self.capacity
        
    def num_cars(self):
        return len(self.plazas)
        
    def get_free_spaces(self):
        return self.capacity - len(self.plazas)
    
    pass
