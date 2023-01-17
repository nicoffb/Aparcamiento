import pickle
import random
import datetime
from aticket import Ticket

class Parking:
    def __init__(self, capacity):
        self.capacity_types = {"car": round(capacity*0.7), "motorcycle": round(capacity*0.15), "handicapped": round(capacity*0.15)}
        self.occupied_types = {"car": 0, "motorcycle": 0, "handicapped": 0}
        self.plazas_ocupadas = {}
        self.tickets = {}
        self.cobros = []
        self.tarifas_vehiculos = {"car": 0.12, "motorcycle": 0.08, "handicapped": 0.10}
        

    def asignar_plaza(self, matricula, tipo_vehiculo):
        if tipo_vehiculo in self.capacity_types:
            if self.capacity_types[tipo_vehiculo] > self.occupied_types[tipo_vehiculo]:
                pin = random.randint(1, 1000)
                plaza = self.occupied_types[tipo_vehiculo] + 1
                fecha_deposito = datetime.datetime.now()
                ticket = Ticket(matricula, fecha_deposito, plaza, pin)
                self.tickets[matricula] = ticket
                self.plazas_ocupadas[matricula] = {"plaza":plaza, "tipo":tipo_vehiculo}
                self.occupied_types[tipo_vehiculo] += 1
                with open("tickets.pickle", "wb") as handle:
                    pickle.dump(self.tickets, handle)
                print("Ticket generado: ")
                print(f"matricula: {ticket.matricula} fecha_deposito: {ticket.fecha_deposito} plaza: {ticket.plaza} pin: {ticket.pin}")
                return f"Se ha asignado una plaza de {tipo_vehiculo} a la matrícula {matricula}."
            else:
                return f"Lo siento, no hay plazas de {tipo_vehiculo} disponibles en este momento."

    
    def get_free_spaces(self):
        free_spaces = {"car": self.capacity_types["car"] - self.occupied_types["car"],
                       "motorcycle": self.capacity_types["motorcycle"] - self.occupied_types["motorcycle"],
                       "handicapped": self.capacity_types["handicapped"] - self.occupied_types["handicapped"]}
        return free_spaces

    def calcular_coste(self, matricula, plaza, pin):
        
        if matricula in self.tickets and self.tickets[matricula].plaza == plaza and self.tickets[matricula].pin == pin:
            tiempo_estacionado = datetime.datetime.now() - self.tickets[matricula].fecha_deposito

            print(f"{matricula}{plaza}{pin}")
            print(f"Has estado {tiempo_estacionado.seconds/60} minutos , que con tu tarifa cada minuto vale tal")
            
            coste = tiempo_estacionado.seconds/60 * self.tarifas_vehiculos[self.plazas_ocupadas[matricula]["tipo"]] 
            print(f"El costo total a pagar es de {coste} €")

            self.occupied_types[self.plazas_ocupadas[matricula]["tipo"]] -= 1
            del self.plazas_ocupadas[matricula]

            print("Ticket generado: ")
            print(f"matricula: {matricula} fecha_deposito: {self.tickets[matricula].fecha_deposito} plaza: {plaza} pin: {pin} fecha de salida {datetime.datetime.now()}")

            with open("tickets.pickle", "wb") as handle:
                pickle.dump(self.tickets, handle)
        else:
            print("Los datos introducidos no son válidos.")

        