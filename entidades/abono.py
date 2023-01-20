import datetime

class Abono:
    def __init__(self, tipo_abono, fecha_activacion,id_plaza_abono):
        self.__tipo_abono = tipo_abono
        self.__fecha_activacion = fecha_activacion
        self.__id_plaza_abono = id_plaza_abono
        
        # Diccionario para almacenar los diferentes tipos de abono y sus duraciones
        self.duraciones = {"mensual": 30, "trimestral": 90, "semestral": 180, "anual": 365}
        
        # Establece la fecha de cancelacion a partir del tipo de abono
        self.__fecha_cancelacion = fecha_activacion + datetime.timedelta(days=self.duraciones[tipo_abono])

    def __str__(self):
        return "Tipo de abono: {}\nFecha de activación: {}\nFecha de cancelación: {}".format(self.__tipo_abono, self.__fecha_activacion, self.__fecha_cancelacion,self.__id_plaza_abono)
        
    @property
    def tipo_abono(self):
        return self.__tipo_abono
   
    @tipo_abono.setter
    def tipo_abono(self, tipo_abono):
        self.__tipo_abono = tipo_abono
        
    @property
    def fecha_activacion(self):
        return self.__fecha_activacion
   
    @fecha_activacion.setter
    def fecha_activacion(self, fecha_activacion):
        self.__fecha_activacion = fecha_activacion
        
    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion
   
    @fecha_cancelacion.setter
    def fecha_cancelacion(self, fecha_cancelacion):
        self.__fecha_cancelacion = fecha_cancelacion
    
    @property
    def id_plaza_abono(self):
        return self.__id_plaza_abono
   
    @id_plaza_abono.setter
    def fid_plaza_abono(self, id_plaza_abono):
        self.__id_plaza_abono = id_plaza_abono