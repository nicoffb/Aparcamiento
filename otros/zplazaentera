from datetime import datetime
class Plaza:
    def __init__(self,id, vehiculo, cliente, pin, entrada=datetime.now(), salida=None, costeTotal=None, ocupada=False):
        self.id= id
        self.__vehiculo = vehiculo
        self.__cliente = cliente
        self.__pin = pin
        self.__entrada = entrada
        self.__salida = salida
        self.__ocupada = ocupada
        self.__costeTotal = costeTotal

    def __str__(self):
        return f"Entrada: {self.entrada}, Matrícula del vehículo: {self.cliente.matricula}, Clave pin: {self.pin}, Número de plaza"

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
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

    @property
    def costeTotal(self):
        return self.__costeTotal

    @costeTotal.setter
    def costeTotal(self, costeTotal):
        self.__costeTotal = costeTotal