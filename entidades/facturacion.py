class Facturacion:
    def __init__(self):
        self._tickets = []
        self.listaAbonados = []

    def add_ticket(self, ticket):
        self._tickets.append(ticket)

    def remove_ticket(self, ticket):
        self._tickets.remove(ticket)

    def get_tickets(self):
        return self._tickets

    def set_tickets(self, tickets):
        self._tickets = tickets

    def add_abonado(self, abonado):
        self.listaAbonados.append(abonado)

    def remove_abonado(self, abonado):
        self.listaAbonados.remove(abonado)

    def get_abonados(self):
        return self.listaAbonados
    
    def __str__(self):
        return "Facturación: \n" + '\n'.join([str(ticket) for ticket in self._tickets])
