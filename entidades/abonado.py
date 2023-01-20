class Abonado:
    def __init__(self, DNI, nombre, apellidos, tarjeta_credito, tipo_abono, email, pin):
        self._DNI = DNI
        self._nombre = nombre
        self._apellidos = apellidos
        self._tarjeta_credito = tarjeta_credito
        self._tipo_abono = tipo_abono
        self._email = email
        self._pin = pin
        
    @property
    def DNI(self):
        return self._DNI
    
    @DNI.setter
    def DNI(self, value):
        self._DNI = value
        
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
    def tipo_abono(self):
        return self._tipo_abono
    
    @tipo_abono.setter
    def tipo_abono(self, value):
        self._tipo_abono = value
        
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
