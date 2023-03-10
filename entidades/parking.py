import pickle
import random
from datetime import datetime
from entidades.plaza import Plaza
from entidades.ticket import Ticket
from entidades.vehiculo import Vehiculo
from entidades.abonado import Abonado
from entidades.abono import Abono
from entidades.facturacion import Facturacion

class Parking:
    def __init__(self, total_plazas):
        self.total_plazas = total_plazas
        self.facturacion = Facturacion()
        self.coste_plazas_car = 1.20
        self.coste_plazas_motorcycle = 0.08
        self.coste_plaza_handicapped = 0.10
        self.plazas_libres= None
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
            self.plazas.append(Plaza(i, Vehiculo(None, None), Abonado(None,None,None,None,None,None,Vehiculo(None, None)), False))

    def addPlaza(self, plaza):
        self.plazas_libres -= 1
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
        self.plazas_libres = sum(1 for plaza in self.plazas if not plaza.ocupada)
        return self.plazas_libres

    def plazas_disponibles_por_tipo(self):
        return {'car': self.plazas_disponibles_car, 'motorcycle': self.plazas_disponibles_motorcycle, 'handicapped': self.plazas_disponibles_handicapped}

    def depositar_vehiculo(self, matricula, tipo):
        plaza_encontrada = False
        for plaza in self.plazas:
            if plaza.ocupada == False and not plaza_encontrada:
                plaza.vehiculo = Vehiculo(matricula, tipo)
                self.addPlaza(plaza)
                print(self.plazas_disponibles_por_tipo())
                pin = random.randint(000000, 9999999)
                ticket = Ticket(plaza.vehiculo, plaza, None, None, None, pin)
                with open("ticket.pkl", "wb") as f:
                    pickle.dump(ticket, f)
                print(f"Se ha generado una plaza {ticket.plaza.vehiculo.tipo} para la matr??cula {ticket.plaza.vehiculo.matricula}. Su pin es: {ticket.pin} para la plaza con el identificador {ticket.plaza.id}. Hora: {ticket.fecha_entrada}")
                self.facturacion.add_ticket(ticket)
                #EL TICKET TEMPORAL SE A??ADE A FACTURACI??N
                f.close()
                plaza_encontrada = True

        if not plaza_encontrada:
            print("No hay plazas disponibles para ese tipo de veh??culo.")
            print(self.plazas_disponibles_por_tipo())


    def removePlaza(self, plaza):
        self.plazas_libres += 1
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
            print("No se ha encontrado una plaza v??lida.")

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
        print (f"Su coste por ser un vehiculo tipo {ticketNuevo.plaza.vehiculo.tipo} para la matr??cula {ticketNuevo.plaza.vehiculo.matricula} es de {ticketNuevo.coste_total}. Su pin era: {ticketNuevo.pin} para la plaza con el identificador {ticketNuevo.plaza.id}. Ha estado de {ticketNuevo.fecha_entrada} a {ticketNuevo.fecha_salida}")
        # hacer que te diga tambi??n la tarifa que es un atributo self.coste.cars pero seria con if supongo con 3 prints
        print("-----------")


    
    

#M??TODOS ABONADOS

    def depositar_abonados(self,matricula,dni):
        plaza_encontrada = False
        for plaza in self.plazas:
            if plaza.ocupada == False and not plaza_encontrada and self.plazas_libres > 0:
                for i, p in enumerate(self.plazas):
                    if p.vehiculo.matricula == matricula and p.abonado.dni == dni:
                        self.addPlaza(p)
                        plaza_encontrada = True
                    #LO SUYO ES QUE ACTUALICE EL LA CANTIDAD DE TIPO DE VEHICULO

            else: 
                print("Plaza ocupada. o no encontrada o lleno")
                print(self.plazas_disponibles_por_tipo())


    

    def retirar_abonados(self,matricula,id,pin):
        i = 0
        encontrado = False
        while i < len(self.plazas) and not encontrado:
            if self.plazas[i].vehiculo.matricula == matricula and self.plazas[i].id == id and self.plazas[i].abonado.pin == pin:
                self.removePlaza(self.plazas[i])    
                encontrado = True
            i += 1
            print("Se ha retirado con ??xito")
        if not encontrado:
            print("La plaza con id {} no existe o el pin no escorrecto.".format(id))



    def alta_abonado(self,idPlaza,nombre,apellidos,dni,tarjeta,tipoAbono,email,matricula,tipoVehiculo):
        vehiculoAbonado = Vehiculo(matricula,tipoVehiculo)
        
        abonoProvisional= Abono(tipoAbono,datetime.now(),idPlaza)

        abonadoProvisional = Abonado(nombre,apellidos,dni,tarjeta,abonoProvisional,email,vehiculoAbonado)
        
        i = 0
        encontrado = False
        while i < len(self.plazas):
            if self.plazas[i].id == idPlaza and self.plazas[i].abonado.activo == False:
                self.plazas[i].vehiculo = vehiculoAbonado
                self.plazas[i].dni = dni
                self.plazas[i].abonado= abonadoProvisional
                self.plazas[i].abonado.activo = True
                encontrado = True
                print("Se ha dado de alta correctamente")
            i += 1  
        if not encontrado:
            print("La plaza con id {} no existe.".format(id))
        self.facturacion.add_abonado(abonadoProvisional)


   
   
   
    def baja_abonado(self,dni):
        i = 0
        encontrado = False
        while i < len(self.plazas) and not encontrado:
            if self.plazas[i].abonado.dni == dni:
                self.plazas[i].vehiculo=None
                self.plazas[i].abonado=None
                encontrado = True
            i += 1
        if not encontrado:
            print("No existe plaza con este DNI: {}".format(id))


    def solicitar_datos_abonado(self):
        idPlaza = int(input("Ingresa el id de la plaza: "))
        nombre = input("Ingresa el nombre del abonado: ")
        apellidos = input("Ingresa los apellidos del abonado: ")
        dni = input("Ingresa el DNI del abonado: ")
        tarjeta = input("Ingresa el numero de tarjeta del abonado: ")
        tipoAbono = input("Ingresa el tipo de abono: mensual, trimestral, semestral u anual ")
        email = input("Ingresa el correo electr??nico del abonado: ")
        matricula = input("Ingresa la matr??cula del veh??culo: ")
        tipoVehiculo = input("Ingresa el tipo de veh??culo: ")
        self.alta_abonado(idPlaza,nombre,apellidos,dni,tarjeta,tipoAbono,email,matricula,tipoVehiculo)


    
    def imprimir_plazas(self):
        for plaza in self.plazas:
            print("Id: ", plaza.id)
            print("Matr??cula: ", plaza.vehiculo.matricula)
            print("Tipo: ", plaza.vehiculo.tipo)
            print("Estado: ", "Ocupada" if plaza.ocupada else "Libre")
        
    
    def imprimir_plazas_con_abonados(self):
        for plaza in self.plazas:
            print("Id: ", plaza.id)
            print("Matr??cula: ", plaza.vehiculo.matricula)
            print("Tipo: ", plaza.vehiculo.tipo)
            print("Estado: ", "Ocupada" if plaza.ocupada else "Libre")
            if plaza.abonado is not None:
                print("INFORMACI??N DEL ABONADO:",plaza.abonado.str() )
            else:
                print("SIN ABONADO ASIGNADO")

    #podria hacer que administradorservice herede pa usar este m??todo