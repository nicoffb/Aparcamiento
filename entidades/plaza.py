
class Plaza:
    def __init__(self,id, vehiculo, abonado=None, ocupada=None):
        self.id= id
        self.__vehiculo = vehiculo
        self.__abonado = abonado
        self.__ocupada = ocupada
        

    def __str__(self):
        return f"Ocupada: {self.ocupada}, Matrícula del vehículo: {self.abonado.matricula}, Plaza: {self.id}, Número de plaza"

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def abonado(self):
        return self.__abonado

    @abonado.setter
    def abonado(self, abonado):
        self.__abonado = abonado


    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

   