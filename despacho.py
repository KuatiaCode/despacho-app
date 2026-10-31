# aplicacion de despacho de pedidos

# ------ funciones -----

def apilar_cajas(pila_cajas: list):
    # Se pide el nombre de la caja y se agrega al final de la lista, como si se pusiera encima de las otras cajas
    caja = input("Ingrese el identificador de la caja (ej. Caja-101): ").strip()
    if caja == "":
        print("[!] Error: El identificador de la caja no puede estar vacío.")
        return
    pila_cajas.append(caja)
    print(f"-> Caja [{caja}] apilada con éxito.")

def retirar_caja(pila_cajas: list):
    # Si no hay ninguna caja, se muestra un aviso y no se intenta sacar nada, así el programa no se cierra con un error
    if len(pila_cajas) == 0:
        print("[!] Error: El almacén está vacío (no hay cajas que retirar).")
        return
    # pop() saca la última caja que se agregó, porque en una pila siempre sale primero la que entró último
    caja = pila_cajas.pop()
    print(f"-> Caja [{caja}] retirada de la cima.")


def formar_camion(cola_camiones: list):
    # Se pide la placa o identificador del camión y se quitan los espacios de más
    camion = input("Ingrese la placa o identificador del vehículo (ej. Camión-Alfa): ").strip()
    # Si el usuario no escribe nada, se muestra un aviso y el camión no se agrega a la cola
    if camion == "":
        print("[!] Error: El identificador del vehículo no puede estar vacío.")
        return
    # append() agrega el camión al final de la cola, respetando el orden de llegada
    cola_camiones.append(camion)
    print(f"-> Camión [{camion}] formado en la fila.")

def salida_camion(cola_camiones: list):
    # Si no hay ningún camión, se muestra un aviso y no se intenta retirar nada
    if len(cola_camiones) == 0:
        print("[!] Error: No hay camiones esperando turno.")
        return
    # pop(0) retira el primer camión que llegó, porque en una cola siempre sale primero el que llegó primero
    camion = cola_camiones.pop(0)
    print(f"-> Camión [{camion}] despachado.")

def estado(pila_cajas: list, cola_camiones: list):
    print("\nESTADO ACTUAL:")
    print(f"- Cajas apiladas (Cima -> Base): {list(reversed(pila_cajas))}")
    print(f"- Fila de camiones (Frente -> Fin): {list(cola_camiones)}")

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
