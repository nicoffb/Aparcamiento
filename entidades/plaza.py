from datetime import datetime
class Plaza:
    def __init__(self,id, vehiculo, cliente, ocupada=False):
        self.id= id
        self.__vehiculo = vehiculo
        self.__cliente = cliente
        self.__ocupada = ocupada
        

    def __str__(self):
        return f"Ocupada: {self.ocupada}, Matrícula del vehículo: {self.cliente.matricula}, Plaza: {self.id}, Número de plaza"

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
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

   