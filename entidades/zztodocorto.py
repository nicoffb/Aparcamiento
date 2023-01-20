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
        for i in range(total_plazas):
            self.plazas.append(Plaza(i, None, None, False))

class Plaza:
    def __init__(self,id, vehiculo, cliente=None, ocupada=None):
        self.id= id
        self.__vehiculo = vehiculo
        self.__cliente = cliente
        self.__ocupada = ocupada

class Vehiculo:
    def __init__(self, matricula, tipo):
        self._matricula = matricula
        self._tipo = tipo

class Ticket:
    def __init__(self, vehiculo, plaza, fecha_entrada, fecha_salida, coste_total,pin):
        self.__vehiculo = vehiculo
        self.__plaza = plaza
        self.__fecha_entrada = datetime.now()
        self.__fecha_salida = fecha_salida
        self.__coste_total = coste_total
        self.__pin = pin