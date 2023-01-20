import random


class Abonado:
    def __init__(self, dni, nombre, apellidos, tarjeta_credito, abono, email,vehiculoAbonado):
        self._vehiculoAbonado = vehiculoAbonado
        self._dni = dni
        self._nombre = nombre
        self._apellidos = apellidos
        self._tarjeta_credito = tarjeta_credito
        self._abono = abono
        self._email = email
        self._pin = random.randint(1111, 9999)
        self._activo = False
        #QUIERO QUE PIN SEA UN NÚMERO AL AZAR PERO DISTINTO ENTRE SÍ

    @property
    def vehiculoAbonado(self):
        return self._vehiculoAbonado
    
    @vehiculoAbonado.setter
    def vehiculo(self, value):
        self._vehiculoAbonado = value
        

    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, value):
        self._dni = value
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    @property
    def apellidos(self):
        return self._apellidos
    
    @apellidos.setter
    def apellidos(self, value):
        self._apellidos = value
        
    @property
    def tarjeta_credito(self):
        return self._tarjeta_credito
    
    @tarjeta_credito.setter
    def tarjeta_credito(self, value):
        self._tarjeta_credito = value
        
    @property
    def abono(self):
        return self._abono
    
    @abono.setter
    def abono(self, value):
        self._abono = value
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
        
    @property
    def pin(self):
        return self._pin
    
    @pin.setter
    def pin(self, value):
        self._pin = value

    @property
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, value):
        self._activo = value

    
    def str(self):
        return "DNI: {}\nNombre: {}\nApellidos: {}\nTarjeta de crédito: {}\nTipo de abono: {}\nEmail: {}\nPin: {}\nAparcamiento reservado: {}\n Matrícula {} Tipo {}".format(self._dni, self._nombre, self._apellidos, self._tarjeta_credito, self._abono, self._email, self._pin, self._activo,self._vehiculoAbonado.matricula,self._vehiculoAbonado.tipo)