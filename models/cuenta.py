class Cuenta:
    def __init__(self, nrocuenta:int, monto:int):
        self.nrocuenta = nrocuenta
        self._monto = monto

    @property
    def nrocuenta(self):
        return self.__nrocuenta
    
    @property
    def monto(self):
        return self.__monto