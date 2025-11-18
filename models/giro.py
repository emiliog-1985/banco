class Giro:
    def __init__(self, id, nroCuenta, cargo, saldo):
        self.id = id
        self.nroCuenta = nroCuenta
        self.cargo = cargo
        self.saldo = saldo
        
        @property
        def id(self):
            return self._id
        
        @property
        def nroCuenta(self):
            return self._nroCuenta
        
        @property
        def cargo(self):
            return self._cargo
        
        @property
        def saldo(self):
            return self._saldo  