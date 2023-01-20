class Facturacion:
    def __init__(self):
        self._tickets = []

    def add_ticket(self, ticket):
        self._tickets.append(ticket)

    def remove_ticket(self, ticket):
        self._tickets.remove(ticket)

    def get_tickets(self):
        return self._tickets

    def set_tickets(self, tickets):
        self._tickets = tickets

    def __str__(self):
        return "Facturación: \n" + '\n'.join([str(ticket) for ticket in self._tickets])
