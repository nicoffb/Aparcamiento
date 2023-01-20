import pickle
import random
from datetime import datetime
from entidades.plaza import Plaza
from entidades.ticket import Ticket
from entidades.vehiculo import Vehiculo


class Parking:
    def __init__(self, total_plazas):
        self.total_plazas = total_plazas
        self.coste_plazas_car = 1.20
        self.coste_plazas_motorcycle = 0.08
        self.coste_plaza_handicapped = 0.10
        self.porcentaje_plazas_libres_car = 0.7
        self.porcentaje_plazas_libres_motorcycle = 0.15
        self.porcentaje_plazas_libres_handicapped = 0.15
        self.plazas_disponibles_car = round(
            self.total_plazas * self.porcentaje_plazas_libres_car)
        self.plazas_disponibles_motorcycle = round(
            self.total_plazas * self.porcentaje_plazas_libres_motorcycle)
        self.plazas_disponibles_handicapped = round(
            self.total_plazas * self.porcentaje_plazas_libres_handicapped)
        self.plazas = []
        for i in range(self.total_plazas):
            self.plazas.append(Plaza(i, Vehiculo(None, None), None, False))

    def addPlaza(self, plaza):
        if plaza.vehiculo.tipo == "car" and self.plazas_disponibles_car > 0:
            self.plazas_disponibles_car -= 1
            plaza.ocupada = True
            for i, p in enumerate(self.plazas):
                if p.id == plaza.id:
                    self.plazas[i] = plaza
        elif plaza.vehiculo.tipo == "motorcycle" and self.plazas_disponibles_motorcycle > 0:
            self.plazas_disponibles_motorcycle -= 1
            plaza.ocupada = True
            for i, p in enumerate(self.plazas):
                if p.id == plaza.id:
                    self.plazas[i] = plaza
        elif plaza.vehiculo.tipo == "handicapped" and self.plazas_disponibles_handicapped > 0:
            self.plazas_disponibles_handicapped -= 1
            plaza.ocupada = True
            for i, p in enumerate(self.plazas):
                if p.id == plaza.id:
                    self.plazas[i] = plaza
                   


    def calcular_plazas_libres(self):
        self.total_plazas = self.plazas_disponibles_car + \
            self.plazas_disponibles_motorcycle + self.plazas_disponibles_handicapped
        return self.total_plazas

    def plazas_disponibles_por_tipo(self):
        return {'car': self.plazas_disponibles_car, 'motorcycle': self.plazas_disponibles_motorcycle, 'handicapped': self.plazas_disponibles_handicapped}

    def asignar_plaza(self, matricula, tipo):
        plaza_encontrada = False
        for plaza in self.plazas:
            if plaza.ocupada == False and not plaza_encontrada:
                plaza.vehiculo = Vehiculo(matricula, tipo)
                self.addPlaza(plaza)
                plaza_encontrada = True
                print(self.plazas_disponibles_por_tipo())
                pin = random.randint(1, 10)
                #corregir el numero
                ticket = Ticket(plaza.vehiculo, plaza, None, None, None, pin)
                with open("ticket.pkl", "wb") as f:
                    pickle.dump(ticket, f)
                print(f"Se ha generado una plaza {ticket.plaza.vehiculo.tipo} para la matrícula {ticket.plaza.vehiculo.matricula}. Su pin es: {ticket.pin} para la plaza con el identificador {ticket.plaza.id}. Hora: {ticket.fecha_entrada}")
                f.close()

        if not plaza_encontrada:
            print("No hay plazas disponibles para ese tipo de vehículo.")
            print(self.plazas_disponibles_por_tipo())


    def removePlaza(self, plaza):
        if plaza in self.plazas:
            plaza.ocupada = False
            if plaza.vehiculo.tipo == "car":
                self.plazas_disponibles_car += 1
            elif plaza.vehiculo.tipo == "motorcycle":
                self.plazas_disponibles_motorcycle += 1
            elif plaza.vehiculo.tipo == "handicapped":
                self.plazas_disponibles_handicapped += 1
        else:
            print("La plaza no existe en el parking.")

    def retirarVehiculo(self, matricula,id,pin):
        with open("ticket.pkl", "rb") as f:
            ticket_recuperado = pickle.load(f)
        plaza_encontrada = False
        for plaza in self.plazas:
            if plaza.vehiculo.matricula == matricula and plaza.id == id and ticket_recuperado.pin == pin:
                plaza.vehiculo.tipo = None
                plaza.vehiculo.matricula = None
                self.removePlaza(plaza)
                plaza_encontrada = True
                print("La plaza ha sido desasignada correctamente.")
                self.calcularPago(ticket_recuperado.vehiculo.tipo)
                f.close()
                
        if not plaza_encontrada:
            print("No se ha encontrado una plaza válida.")

    def calcularPago(self,tipo):
        with open("ticket.pkl", "rb") as f:
            ticket_recuperado = pickle.load(f)
        ticket_recuperado.fecha_salida= datetime.now()
        tiempo_estacionado = ticket_recuperado.fecha_salida - ticket_recuperado.fecha_entrada
        print(tiempo_estacionado.seconds/60)
        print(" de tiempo estacionado ")
        
        if tipo == "car":
            resultado = (tiempo_estacionado.seconds/60)*self.coste_plazas_car
        elif tipo == "motorcycle":
            resultado=tiempo_estacionado.seconds/60* self.coste_plazas_motorcycle
        elif tipo == "handicapped":
            resultado=tiempo_estacionado.seconds/60* self.coste_plaza_handicapped
        else:
            print("No existe ese tipo")

        
        ticketNuevo = Ticket(ticket_recuperado.vehiculo,ticket_recuperado.plaza,ticket_recuperado.fecha_entrada,ticket_recuperado.fecha_salida,resultado,ticket_recuperado.pin)
        with open("ticket.pkl", "wb") as f:
            pickle.dump(ticketNuevo, f)
        
        print("-----------")
        print (f"Su coste por ser un vehiculo tipo {ticketNuevo.plaza.vehiculo.tipo} para la matrícula {ticketNuevo.plaza.vehiculo.matricula} es de {ticketNuevo.coste_total}. Su pin era: {ticketNuevo.pin} para la plaza con el identificador {ticketNuevo.plaza.id}. Ha estado de {ticketNuevo.fecha_entrada} a {ticketNuevo.fecha_salida}")
        # hacer que te diga también la tarifa que es un atributo self.coste.cars pero seria con if supongo con 3 prints
        print("-----------")
        #RECORDAR GUARDAR EN UNA LISTA DE TICKETS QUE PODRIA SER FACTURACION CON LISTA DE TICKETS
        #guardar en lista lista de tickets de facturacion con append lista(ticket)

    def imprimir_plazas(self):
        for plaza in self.plazas:
            print("Id: ", plaza.id)
            print("Matrícula: ", plaza.vehiculo.matricula)
            print("Tipo: ", plaza.vehiculo.tipo)
            print("Estado: ", "Ocupada" if plaza.ocupada else "Libre")
            print("")
