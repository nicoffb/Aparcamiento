class Vehiculo:
    def __init__(self, matricula, tipo):
        self._matricula = matricula
        self._tipo = tipo

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value