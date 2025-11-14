import os
import colorama


def menu_principal():
    while True:
        os.system('clear')
        print(colorama.Fore.CYAN + "==============================" + colorama.Style.RESET_ALL)
        print(colorama.Fore.CYAN + "========Menú Principal========" + colorama.Style.RESET_ALL)
        print(colorama.Fore.CYAN + "==============================" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "1. Realizar un giro 💰  === >" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "2. Listar giros 📝 ======== >" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "3. Mostrar saldo 💵 ======= >" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + "4. Salir 🚪 =============== >" + colorama.Style.RESET_ALL)
        print(colorama.Fore.CYAN + "==============================" + colorama.Style.RESET_ALL)

        opcion = input(colorama.Fore.YELLOW + "Seleccione una opción: " + colorama.Style.RESET_ALL)
        os.system('clear')

        if opcion == '1':
            realizar_giro()
        elif opcion == '2':
            listar_giros()
        elif opcion == '3':
            mostrar_saldo()
        elif opcion == '4':
            print(colorama.Fore.MAGENTA + "Saliendo de la aplicación. ¡Hasta luego! 👋" + colorama.Style.RESET_ALL)
            break
        else:
            print(colorama.Fore.RED + "Opción inválida. Por favor, intente de nuevo." + colorama.Style.RESET_ALL)
            input("Presione Enter para continuar...")

menu_principal()