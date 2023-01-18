class Ticket:
    def __init__(self, matricula, fecha_deposito, plaza, pin):
        self.matricula = matricula
        self.fecha_deposito = fecha_deposito
        self.plaza = plaza
        self.pin = pin
        self.fecha_salida = None
        self.coste = None