# aplicacion de despacho de pedidos

# ------ funciones -----

def apilar_cajas(pila_cajas: list):
    pass

def retirar_caja(pila_cajas: list):
    pass

def formar_camion(cola_camiones: list):
    pass

def salida_camion(cola_camiones: list):
    pass

def estado(pila_cajas: list, cola_camiones: list):
    pass

# ----- main -----

def main():
    
    pila_cajas = []
    cola_camiones = []

    while True:
        print("--- Sistema Logística CLI ---")
        print("1. Apilar cajas")
        print("2. Retirar caja")
        print("3. Formar camión")
        print("4. Salida de camión")
        print("5. Estado")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            apilar_cajas(pila_cajas)

        elif opcion == "2": 
            retirar_caja(pila_cajas)

        elif opcion == "3":
            formar_camion(cola_camiones)

        elif opcion == "4":
            salida_camion(cola_camiones)

        elif opcion == "5":
            estado(pila_cajas, cola_camiones)

        elif opcion == "6":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nError: Opción inválida. Por favor, seleccione una opción válida")

    if __name__ == "__main__":
        main()
