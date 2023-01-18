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