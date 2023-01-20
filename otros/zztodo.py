from vehiculo import Vehiculo


from plaza import Plaza

class Parking:
    def __init__(self,total_plazas):
        self.total_plazas = total_plazas
        self.porcentaje_plazas_libres_car = 0.7
        self.porcentaje_plazas_libres_motorcycle = 0.15
        self.porcentaje_plazas_libres_handicapped = 0.15
        self.plazas_libres_car = round(self.total_plazas * self.porcentaje_plazas_libres_car)
        self.plazas_libres_motorcycle = round(self.total_plazas * self.porcentaje_plazas_libres_motorcycle)
        self.plazas_libres_handicapped = round(self.total_plazas * self.porcentaje_plazas_libres_handicapped)
        self.plazas = []
        for i in range(total_plazas):
            self.plazas.append(Plaza(i, None, None, None, None, None, None, False))


    def addPlaza(self, plaza):
        plaza.ocupado = True
        if plaza.vehiculo.tipo == "car":
            self.plazas_libres_car -= 1
        elif plaza.vehiculo.tipo == "motorcycle":
            self.plazas_libres_motorcycle -= 1
        elif plaza.vehiculo.tipo == "handicapped":
            self.plazas_libres_handicapped -= 1
        self.plazas.append(plaza)

    def liberarPlaza(self, plaza):
        plaza.ocupado = False
        if plaza.vehiculo.tipo == "car":
            self.plazas_libres_car += 1
        elif plaza.vehiculo.tipo == "motorcycle":
            self.plazas_libres_motorcycle += 1
        elif plaza.vehiculo.tipo == "handicapped":
            self.plazas_libres_handicapped += 1
        self.plazas.remove(plaza)

    def asignar_plaza(self, matricula, tipo_vehiculo):
        plaza_asignada = None
        vehiculo = Vehiculo(matricula, tipo_vehiculo)
        if vehiculo.tipo == "car" and self.plazas_libres_car > 0:
            for plaza in self.plazas:
                if not plaza.ocupada and plaza.vehiculo.tipo == "car":
                    plaza.ocupada = True
                    plaza.vehiculo = vehiculo
                    plaza_asignada = plaza
                    self.plazas_libres_car -= 1
                    break
        elif vehiculo.tipo == "motorcycle" and self.plazas_libres_motorcycle > 0:
            for plaza in self.plazas:
                if not plaza.ocupada and plaza.vehiculo.tipo == "motorcycle":
                    plaza.ocupada = True
                    plaza.vehiculo = vehiculo
                    plaza_asignada = plaza
                    self.plazas_libres_motorcycle -= 1
                    break
        elif vehiculo.tipo == "handicapped" and self.plazas_libres_handicapped > 0:
            for plaza in self.plazas:
                if not plaza.ocupada and plaza.vehiculo.tipo == "handicapped":
                    plaza.ocupada = True
                    plaza.vehiculo = vehiculo
                    plaza_asignada = plaza
                    self.plazas_libres_handicapped -= 1
                    break
        return plaza_asignada




    def generar_ticket(self):
        import random
        pin = random.randint(100000, 999999)
        ticket = Ticket(self.plaza_asignada.vehiculo, self.plaza_asignada, self.fecha_entrada, self.fecha_deposito, pin)
        print(ticket)
        print(ticket.__str__())


class Plaza:
    def __init__(self,id, vehiculo, cliente, ocupada=False):
        self.id= id
        self.__vehiculo = vehiculo
        self.__cliente = cliente
        self.__ocupada = ocupada
        

    def __str__(self):
        return f"Ocupada: {self.ocupada}, Matrícula del vehículo: {self.cliente.matricula}, Plaza: {self.id}, Número de plaza"

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente


    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada


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

class Ticket:
    def __init__(self, vehiculo, plaza, fecha_entrada, fecha_salida, coste_total,pin):
        self.__vehiculo = vehiculo
        self.__plaza = plaza
        self.__fecha_entrada = datetime.now()
        self.__fecha_salida = fecha_salida
        self.__coste_total = coste_total
        self.__pin = pin

    def __str__(self):
        return f"Se ha generado una plaza {self.plaza.id} para la matrícula {self.vehiculo.matricula}. Su pin es: {self.id}"


    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def coste_total(self):
        return self.__coste_total

    @coste_total.setter
    def coste_total(self, coste_total):
        self.__coste_total
    
    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin
