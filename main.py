import os # Importa el módulo os para interactuar con el sistema operativo
import colorama # Importa colorama para colores en la terminal
from dao.CuentaDAO import CuentaDAO # Importa la clase CuentaDAO para manejar las cuentas
from dao.GiroDAO import GiroDAO   # Importa la clase GiroDAO para manejar los giros
from models.cuenta import Cuenta  # Importa la clase Cuenta para representar una cuenta bancaria
from models.giro import Giro      # Importa la clase Giro para representar un giro bancario
from models.conectar import conectar # Importa la clase de conexion a la base de datos

def validar_saldo():
    print(colorama.Fore.YELLOW + "==== Validar Saldo ====" + colorama.Style.RESET_ALL)
    nroCuenta = input(colorama.Fore.CYAN + "Ingrese el número de cuenta: " + colorama.Style.RESET_ALL)
    GiroDAO = CuentaDAO()
    monto = GiroDAO.mostrar_saldo(nroCuenta)
    if monto is not None:
        print(colorama.Fore.GREEN + f"El monto disponible en la cuenta {nroCuenta} es: ${monto} pesos" + colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.RED + "Número de cuenta no encontrado." + colorama.Style.RESET_ALL)
    input(colorama.Fore.YELLOW + "Presione Enter para continuar..." + colorama.Style.RESET_ALL)

def mostrar_cuentas():
    print(colorama.Fore.YELLOW + "==== Mostrar cuentas ====" + colorama.Style.RESET_ALL)
    dao = CuentaDAO()
    cuentas = dao.listar_cuenta()
    print(colorama.Fore.GREEN + "Listado de Cuentas:" + colorama.Style.RESET_ALL)
    if not cuentas:
        print(colorama.Fore.RED + "No hay cuentas registradas." + colorama.Style.RESET_ALL)
    else:
        for cuenta in cuentas:
            print(
                f"Numero de cuenta: {cuenta['nroCuenta']} | Monto: {cuenta['monto']}"
            )
    input(colorama.Fore.YELLOW + "Presione Enter para continuar..." + colorama.Style.RESET_ALL)

def nuevo_deposito():
    print(colorama.Fore.YELLOW + "==== Nuevo Deposito ====" + colorama.Style.RESET_ALL)
    nroCuenta = input(colorama.Fore.CYAN + "Ingrese el número de cuenta de destino: " + colorama.Style.RESET_ALL)
    monto = float(input(colorama.Fore.CYAN + "Ingrese el monto a depositar: " + colorama.Style.RESET_ALL))
    cuenta_dao = CuentaDAO()
    cuenta = cuenta_dao.obtener_cuenta_por_numero(nroCuenta)
    if cuenta is None:
        print(colorama.Fore.RED + "Cuenta no encontrada." + colorama.Style.RESET_ALL)
    else:
        nuevo_monto = cuenta['monto'] + monto
        cuenta_dao.actualizar_monto(nroCuenta, nuevo_monto)
        print(colorama.Fore.GREEN + "Depósito realizado con éxito." + colorama.Style.RESET_ALL)
    input(colorama.Fore.YELLOW + "Presione Enter para continuar..." + colorama.Style.RESET_ALL)



def nuevo_giro():
    print(colorama.Fore.YELLOW + "==== Nuevo Giro ====" + colorama.Style.RESET_ALL)
    nroCuenta = input(colorama.Fore.CYAN + "Ingrese el número de cuenta de origen: " + colorama.Style.RESET_ALL)
    cargo = float(input(colorama.Fore.CYAN + "Ingrese el monto a girar: " + colorama.Style.RESET_ALL))
    giro_dao = GiroDAO()
    giro_dao.insertar_giro(nroCuenta, cargo)
    print(colorama.Fore.GREEN + "Giro realizado con éxito." + colorama.Style.RESET_ALL)
    input(colorama.Fore.YELLOW + "Presione Enter para continuar..." + colorama.Style.RESET_ALL)

def validar_saldo():
    print(colorama.Fore.YELLOW + "==== Validar Saldo ====" + colorama.Style.RESET_ALL)
    nroCuenta = input(colorama.Fore.CYAN + "Ingrese el número de cuenta: " + colorama.Style.RESET_ALL)
    Cuenta_DAO = CuentaDAO()
    monto = Cuenta_DAO.mostrar_saldo(nroCuenta)
    if monto is not None:
        print(colorama.Fore.GREEN + f"El monto disponible en la cuenta {nroCuenta} es: ${monto} pesos" + colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.RED + "Número de cuenta no encontrado." + colorama.Style.RESET_ALL)
    input(colorama.Fore.YELLOW + "Presione Enter para continuar..." + colorama.Style.RESET_ALL)


def mostrar_saldo():
    print(colorama.Fore.YELLOW + "Estimado favor ingrese su número de cuenta para mostrar el saldo." + colorama.Style.RESET_ALL)
    obtener_cuenta_por_numero = input(colorama.Fore.CYAN + "Número de cuenta: " + colorama.Style.RESET_ALL)
    Cuenta_DAO = CuentaDAO()
    monto = Cuenta_DAO.mostrar_saldo(obtener_cuenta_por_numero)
    if monto is not None:
        print(colorama.Fore.GREEN + f"El monto de la cuenta {obtener_cuenta_por_numero} es: ${monto} pesos" + colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.RED + "Número de cuenta no encontrado." + colorama.Style.RESET_ALL)
    input("Presione Enter para continuar...")   


def menu_principal():
    while True:
        os.system('clear')
        print(colorama.Fore.CYAN + "=================================================" + colorama.Style.RESET_ALL)
        print(colorama.Fore.CYAN + "==================Menú Principal=================" + colorama.Style.RESET_ALL)
        print(colorama.Fore.CYAN + "=================================================" + colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTMAGENTA_EX + "Realizar un giro ✔️" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "1. Mostrar todas las cuentas disponibles 💲" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "2. Nuevo giro 🔄" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "3. Nuevo deposito 💸" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "4. Validacion de Saldo 🪙" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN +  "5. Registrar giros 🔄" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "6. Actualizar saldo 🪙" + colorama.Style.RESET_ALL)
        print(colorama.Fore.CYAN + "=================================================" + colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTMAGENTA_EX + "Listar giros ✔️" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "7. Mostrar cuentas 💵" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "8. Ingresar numero de cuenta 🏦" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "9. Mostrar todos los giros de tu cuenta 💰" + colorama.Style.RESET_ALL)
        print(colorama.Fore.CYAN + "=================================================" + colorama.Style.RESET_ALL)
        print(colorama.Fore.LIGHTMAGENTA_EX + "Mostrar saldo ✔️" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "10. Mostrar saldo de una cuenta 💳" + colorama.Style.RESET_ALL)
        print(colorama.Fore.CYAN + "=================================================" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "0. Salir 🚪" + colorama.Style.RESET_ALL)

        opcion = input(colorama.Fore.YELLOW + "Seleccione una opción: " + colorama.Style.RESET_ALL)
        os.system('clear')

        if opcion == '1':
            mostrar_cuentas()
        elif opcion == '2':
            nuevo_giro()
        elif opcion == '3':
            nuevo_deposito()    
        elif opcion == '9':
            mostrar_saldo()
        elif opcion == '10':
            validar_saldo()
        elif opcion == '0':
            print(colorama.Fore.MAGENTA + "Saliendo de la aplicación. ¡Hasta luego! 👋" + colorama.Style.RESET_ALL)
            break
        else:
            print(colorama.Fore.RED + "Opción inválida. Por favor, intente de nuevo." + colorama.Style.RESET_ALL)
            input("Presione Enter para continuar...")

menu_principal()