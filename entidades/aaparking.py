import pickle
import random
from datetime import datetime
from entidades.plaza import Plaza
from entidades.ticket import Ticket
from entidades.vehiculo import Vehiculo


class Parking:
    def __init__(self,total_plazas):
        self.total_plazas = total_plazas
        self.coste_plazas_car=1.20
        self.coste_plazas_motorcycle=0.08
        self.porcentaje_plazas_libres_car = 0.7
        self.porcentaje_plazas_libres_motorcycle = 0.15
        self.porcentaje_plazas_libres_handicapped = 0.15
        self.plazas_disponibles_car = round(self.total_plazas * self.porcentaje_plazas_libres_car)
        self.plazas_disponibles_motorcycle = round(self.total_plazas * self.porcentaje_plazas_libres_motorcycle)
        self.plazas_disponibles_handicapped = round(self.total_plazas * self.porcentaje_plazas_libres_handicapped)
        self.plazas = []
        for i in range(self.total_plazas):
            self.plazas.append(Plaza(i, Vehiculo(None,None), None, False))

    def addPlaza(self, plaza):
        if plaza.vehiculo.tipo == "car" and self.plazas_disponibles_car > 0:
            self.plazas_disponibles_car -= 1
            plaza.ocupada = True
            self.plazas.append(plaza)
        elif plaza.vehiculo.tipo == "motorcycle" and self.plazas_disponibles_motorcycle > 0:
            self.plazas_disponibles_motorcycle -= 1
            plaza.ocupada = True
            self.plazas.append(plaza)
            
        elif plaza.vehiculo.tipo == "handicapped" and self.plazas_disponibles_handicapped > 0:
            self.plazas_disponibles_handicapped -= 1
            plaza.ocupada = True
            self.plazas.append(plaza)
            
        else:
            print("Hola")



    def calcular_plazas_libres(self):
        self.total_plazas = self.plazas_disponibles_car + self.plazas_disponibles_motorcycle + self.plazas_disponibles_handicapped
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
                pin = random.randint(100000, 999999)      
                ticket = Ticket(plaza.vehiculo,plaza,None,None, None, pin)
                print(f"Se ha generado una plaza {ticket.plaza.vehiculo.tipo} para la matrícula {ticket.plaza.vehiculo.matricula}. Su pin es: {ticket.pin}. Hora: {ticket.fecha_entrada}")    
                
        if not plaza_encontrada:
            print("No hay plazas disponibles para ese tipo de vehículo.")
            print(self.plazas_disponibles_por_tipo())


    # def generar_ticket(self):
    #     pin = random.randint(100000, 999999)
    #     ticket = Ticket(self.plaza, self.plaza_asignada, self.fecha_entrada,pin)
    #     print(f"Se ha generado una plaza {ticket.vehiculo.tipo} para la matrícula {ticket.vehiculo.matricula}. Su pin es: {self.pin}")
    #     #print(ticket)
    #     print(ticket.__str__())
        




def removePlaza(self, plaza):
        if plaza in self.plazas:
            self.plazas.remove(plaza)
            plaza.ocupada = False
            if plaza.vehiculo.tipo == "car":
                self.plazas_disponibles_car += 1
            elif plaza.vehiculo.tipo == "motorcycle":
                self.plazas_disponibles_motorcycle += 1
            elif plaza.vehiculo.tipo == "handicapped":
                self.plazas_disponibles_handicapped += 1
        else:
            print("La plaza no existe en el parking.")











    






    

    