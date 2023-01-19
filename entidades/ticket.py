
from datetime import datetime

class Ticket:
    def __init__(self, vehiculo, plaza, fecha_entrada, fecha_salida, coste_total,pin):
        self.__vehiculo = vehiculo
        self.__plaza = plaza
        self.__fecha_entrada = datetime.now()
        self.__fecha_salida = fecha_salida
        self.__coste_total = coste_total
        self.__pin = pin

    def __str__(self):
        return f"Se ha generado una plaza {self.plaza.id} para la matrícula {self.vehiculo.matricula}. Su pin es: {self.pin}"


    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def coste_total(self):
        return self.__coste_total

    @coste_total.setter
    def coste_total(self, coste_total):
        self.__coste_total
    
    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin
