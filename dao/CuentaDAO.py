from models.conectar import conectar # Importa la clase de conexion a la base de datos
# Clase para manejar las operaciones de la tabla 'cuenta' en la base de datos
class CuentaDAO: 
    def __init__(self):
        self.conexion = conectar
        self.conexion = conectar()

# Metodo para obtener una cuenta por su numero de cuenta
    def obtener_cuenta_por_numero(self, nroCuenta):
        sql = "SELECT * FROM cuenta WHERE nroCuenta = %s"
        datos = (nroCuenta,)
        return self.conexion.listar_uno(sql, datos)
    
# Metodo para crear una cuenta
    def crear_cuenta(self, numero_cuenta, titular, monto_inicial):
        sql = "INSERT INTO cuenta (numero_cuenta, titular, monto) VALUES (%s, %s, %s)"
        datos = (numero_cuenta, titular, monto_inicial)
        self.conexion.ejecutar(sql, datos)

# Metodo para actualizar el monto de una cuenta
    def actualizar_monto(self, nroCuenta, nuevo_monto):
        sql = "UPDATE cuenta SET monto = %s WHERE nroCuenta = %s"
        datos = (nuevo_monto, nroCuenta)
        self.conexion.ejecutar(sql, datos)

# Metodo para listar todas las cuenta        
    def listar_cuenta(self):
        sql = "SELECT * FROM cuenta"
        return self.conexion.listar(sql) 
    
# Metodo para obtener el monto de una cuenta
    def mostrar_saldo(self, numero_cuenta):
        sql = "SELECT monto FROM cuenta WHERE nroCuenta = %s"
        datos = (numero_cuenta,)
        resultado = self.conexion.listar_uno(sql, datos)
        if resultado:
            return resultado['monto']
        return None
    