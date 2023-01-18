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


    def addPlaza(self, plaza):
        plaza.ocupado = True
        if plaza.vehiculo.tipo == "car":
            self.plazas_libres_car -= 1
        elif plaza.vehiculo.tipo == "motorcycle":
            self.plazas_libres_motorcycle -= 1
        elif plaza.vehiculo.tipo == "handicapped":
            self.plazas_libres_handicapped -= 1
        self.plazas.append(plaza)

    def liberarPlaza(self, plaza):
        plaza.ocupado = False
        if plaza.vehiculo.tipo == "car":
            self.plazas_libres_car += 1
        elif plaza.vehiculo.tipo == "motorcycle":
            self.plazas_libres_motorcycle += 1
        elif plaza.vehiculo.tipo == "handicapped":
            self.plazas_libres_handicapped += 1
        self.plazas.remove(plaza)


    def plazasLibres(self):
        return len([plaza for plaza in self.plazas if not plaza.ocupado])

    def plazasLibresPorTipo(self):
        plazasLibres = {"car": self.plazas_libres_car, "motorcycle": self.plazas_libres_motorcycle, "handicapped": self.plazas_libres_handicapped}
        for plaza in self.plazas:
            if not plaza.ocupado:
                plazasLibres[plaza.vehiculo.tipo] -= 1
        return plazasLibres

class Plaza:
    def __init__(self, vehiculo, cliente, pin, entrada=datetime.now(), salida=None, costeTotal=None, activo=True):
        self.__vehiculo = vehiculo
        self.__cliente = cliente
        self.__pin = pin
        self.__entrada = entrada
        self.__salida = salida
        self.__activo = activo
        self.__costeTotal = costeTotal

    def __str__(self):
        return f"Entrada: {self.entrada}, Matrícula del vehículo: {self.cliente.matricula}, Clave pin: {self.pin}"

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def entrada(self):
        return self.__entrada

    @entrada.setter
    def entrada(self, entrada):
        self.__entrada = entrada

    @property
    def salida(self):
        return self.__salida

    @salida.setter
    def salida(self, salida):
        self.__salida = salida

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, activo):
        self.__activo = activo

    @property
    def costeTotal(self):
        return self.__costeTotal

    @costeTotal.setter
    def costeTotal(self, costeTotal):
        self.__costeTotal = costeTotal


class Vehiculo:
    def __init__(self, tipo, matricula):
        self._tipo = tipo
        self._matricula = matricula

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value