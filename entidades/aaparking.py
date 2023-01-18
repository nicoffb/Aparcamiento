from vehiculo import Vehiculo

class Parking:
    def __init__(self,total_plazas):
        self.total_plazas = total_plazas
        self.porcentaje_plazas_libres_car = 0.7
        self.porcentaje_plazas_libres_motorcycle = 0.15
        self.porcentaje_plazas_libres_handicapped = 0.15
        self.plazas_libres_car = round(self.total_plazas * self.porcentaje_plazas_libres_car)
        self.plazas_libres_motorcycle = round(self.total_plazas * self.porcentaje_plazas_libres_motorcycle)
        self.plazas_libres_handicapped = round(self.total_plazas * self.porcentaje_plazas_libres_handicapped)
        self.plazas = []

    ...
    def addPlaza(self, plaza):
        plaza.ocupado = True
        self.plazas.append(plaza)

    def liberarPlaza(self, plaza):
        plaza.ocupado = False
        self.plazas.remove(plaza)

    def plazasLibres(self):
        return len([plaza for plaza in self.plazas if not plaza.ocupado])

    def plazasLibresPorTipo(self):
        plazasLibres = {"car": self.plazas_libres_car, "motorcycle": self.plazas_libres_motorcycle, "handicapped": self.plazas_libres_handicapped}
        for plaza in self.plazas:
            if not plaza.ocupado:
                plazasLibres[plaza.vehiculo.tipo] -= 1
        return plazasLibres