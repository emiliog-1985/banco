class Cuenta:
    def __init__(self, nrocuenta, monto):
        self.nrocuenta = nrocuenta
        self._monto = monto

    @property
    def nrocuenta(self):
        return self._nrocuenta
    
    @property
    def monto(self):
        return self._monto