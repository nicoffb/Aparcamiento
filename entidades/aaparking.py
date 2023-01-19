import pickle
import random
from entidades.plaza import Plaza
from entidades.ticket import Ticket
from entidades.vehiculo import Vehiculo


class Parking:
    def __init__(self,total_plazas):
        self.total_plazas = total_plazas
        self.porcentaje_plazas_libres_car = 0.7
        self.porcentaje_plazas_libres_motorcycle = 0.15
        self.porcentaje_plazas_libres_handicapped = 0.15
        self.plazas_disponibles_car = round(self.total_plazas * self.porcentaje_plazas_libres_car)
        self.plazas_disponibles_motorcycle = round(self.total_plazas * self.porcentaje_plazas_libres_motorcycle)
        self.plazas_disponibles_handicapped = round(self.total_plazas * self.porcentaje_plazas_libres_handicapped)
        self.plazas = []
        # for i in range(total_plazas):
        #     tipo = None
        #     vehiculo = None
        #     if i < self.plazas_disponibles_car:
        #         tipo = "car"
        #         vehiculo = Vehiculo(None, tipo)
        #     elif i < self.plazas_disponibles_car + self.plazas_disponibles_motorcycle:
        #         tipo = "motorcycle"
        #         vehiculo = Vehiculo(None, tipo)
        #     else:
        #         tipo = "handicapped"
        #         vehiculo = Vehiculo(None, tipo)
        #     self.plazas.append(Plaza(i, vehiculo, None, False))
        for i in range(total_plazas):
            self.plazas.append(Plaza(i, None, None, False))


    # def addPlaza(self, plaza):
    #     plaza.ocupado = True
    #     if plaza.vehiculo.tipo == "car":
    #         self.plazas_libres_car -= 1
    #     elif plaza.vehiculo.tipo == "motorcycle":
    #         self.plazas_libres_motorcycle -= 1
    #     elif plaza.vehiculo.tipo == "handicapped":
    #         self.plazas_libres_handicapped -= 1
    #     self.plazas.append(plaza)

    # def liberarPlaza(self, plaza):
    #     plaza.ocupado = False
    #     if plaza.vehiculo.tipo == "car":
    #         self.plazas_libres_car += 1
    #     elif plaza.vehiculo.tipo == "motorcycle":
    #         self.plazas_libres_motorcycle += 1
    #     elif plaza.vehiculo.tipo == "handicapped":
    #         self.plazas_libres_handicapped += 1
    #     self.plazas.remove(plaza)


    def addPlaza(self, plaza):
        # if isinstance(plaza, Plaza) and not plaza.ocupada:
            plaza.ocupada = True
            if plaza.vehiculo.tipo == "car":
                self.plazas_disponibles_car -= 1
            elif plaza.vehiculo.tipo == "motorcycle":
                self.plazas_disponibles_motorcycle -= 1
            elif plaza.vehiculo.tipo == "handicapped":
                self.plazas_disponibles_handicapped -= 1
            self.plazas.append(plaza)
        # else:
        #     raise ValueError("La plaza no es valida o ya esta ocupada")


    def plazasLibres(self):
        return len([plaza for plaza in self.plazas if not plaza.ocupada])











    def asignar_plaza(self, matricula, tipo_vehiculo):
        plaza_asignada = None
        vehiculo = Vehiculo(matricula, tipo_vehiculo)
        if vehiculo.tipo == "car" and self.plazas_disponibles_car > 0:
            for plaza in self.plazas:
                if not plaza.ocupada and plaza.vehiculo.tipo == "car":
                    plaza.ocupada = True
                    plaza.vehiculo = vehiculo
                    plaza_asignada = plaza
                    self.plazas_disponibles_car -= 1
                    self.generar_ticket()
        elif vehiculo.tipo == "motorcycle" and self.plazas_disponibles_motorcycle > 0:
            for plaza in self.plazas:
                if not plaza.ocupada and plaza.vehiculo.tipo == "motorcycle":
                    plaza.ocupada = True
                    plaza.vehiculo = vehiculo
                    plaza_asignada = plaza
                    self.plazas_disponibles_motorcycle -= 1
                    self.generar_ticket()
        elif vehiculo.tipo == "handicapped" and self.plazas_disponibles_handicapped > 0:
            for plaza in self.plazas:
                if not plaza.ocupada and plaza.vehiculo.tipo == "handicapped":
                    plaza.ocupada = True
                    plaza.vehiculo = vehiculo
                    plaza_asignada = plaza
                    self.plazas_disponibles_handicapped -= 1
                    self.generar_ticket()
        return plaza_asignada

# # return f"Se ha generado una plaza {self.plaza.id} para la matrícula {self.vehiculo.matricula}. Su pin es: {self.pin}"


#     def generar_ticket(self):
#         pin = random.randint(100000, 999999)
#         ticket = Ticket(self.plaza_asignada.vehiculo, self.plaza_asignada, self.fecha_entrada,pin)
#         print(f"Se ha generado una plaza {ticket.vehiculo.tipo} para la matrícula {ticket.vehiculo.matricula}. Su pin es: {self.pin}")
#         #print(ticket)
#         print(ticket.__str__())
        















    






    def plazasLibresPorTipo(self):
        plazasLibres = {"car": self.plazas_disponibles_car, "motorcycle": self.plazas_disponibles_motorcycle, "handicapped": self.plazas_disponibles_handicapped}
        for plaza in self.plazas:
            if not plaza.ocupada:
                plazasLibres[plaza.vehiculo.tipo] -= 1
        return plazasLibres

    