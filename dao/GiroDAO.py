from models.conectar import conectar # Importa la clase de conexion a la base de datos
# Clase para manejar las operaciones de la tabla 'giros' en la base de datos
class GiroDAO: 
    def __init__(self):
        self.conectar = conectar()

# Metodo para insertar un giro
    def insertar_giro(self, nroCuenta, cargo):
        # 1. Consultar el monto actual
        sql_monto = "SELECT monto FROM cuenta WHERE nroCuenta = %s"
        datos_monto = (nroCuenta,)
        resultado = self.conectar.listar_uno(sql_monto, datos_monto)
        if resultado is None:
            print("Cuenta no encontrada.")
            return False
        monto_actual = resultado['monto']

        # 2. Calcular el nuevo saldo
        saldo = monto_actual - cargo

        # 3. Insertar el giro
        sql_giro = "INSERT INTO giro (nroCuenta, cargo, saldo) VALUES (%s, %s, %s)"
        datos_giro = (nroCuenta, cargo, saldo)
        self.conectar.ejecutar(sql_giro, datos_giro)

        # 4. Actualizar el saldo en la cuenta
        sql_update = "UPDATE cuenta SET monto = %s WHERE nroCuenta = %s"
        datos_update = (saldo, nroCuenta)
        self.conectar.ejecutar(sql_update, datos_update)
        return True

# Metodo para listar todos los giros        
    def listar_giro(self):
        sql = "SELECT * FROM giro"
        return self.conectar.listar(sql)
  