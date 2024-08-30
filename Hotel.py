class Hotel:
    def __init__(self):
        self.habitaciones = {
            'Individual': 50.00,
            'Doble': 80.00,
            'Suite': 120.00
        }
        self.servicios = {
            'Piscina': 15.00,
            'Cancha de Golf': 30.00,
            'Spa': 25.00
        }
        self.reservas = []

    def mostrar_habitaciones(self):
        print("Opciones de Habitaciones:")
        for tipo, precio in self.habitaciones.items():
            print(f"{tipo}: ${precio:.2f} por noche")

    def mostrar_servicios(self):
        print("Servicios adicionales:")
        for servicio, precio in self.servicios.items():
            print(f"{servicio}: ${precio:.2f}")

    def hacer_reserva(self):
        self.mostrar_habitaciones()
        habitacion = input("Elija el tipo de habitación: ")
        noches = int(input("Ingrese el número de noches: "))

        if habitacion not in self.habitaciones:
            print("Tipo de habitación no válido.")
            return

        nombre = input("Ingrese su nombre: ")
        documento = input("Ingrese su documento de identidad: ")

        servicios_elegidos = []
        total_servicios = 0
        while True:
            self.mostrar_servicios()
            servicio = input("Ingrese el servicio adicional que desea (o 'no' para finalizar): ")
            if servicio.lower() == 'no':
                break
            if servicio in self.servicios:
                servicios_elegidos.append(servicio)
                total_servicios += self.servicios[servicio]
            else:
                print("Servicio no válido.")

        costo_habitacion = self.habitaciones[habitacion] * noches
        costo_total = costo_habitacion + total_servicios

        reserva = {
            'Nombre': nombre,
            'Documento': documento,
            'Habitacion': habitacion,
            'Noches': noches,
            'Costo Habitación': costo_habitacion,
            'Servicios': servicios_elegidos,
            'Costo Total': costo_total
        }
        self.reservas.append(reserva)

        print("\n--- Factura Detallada ---")
        print(f"Cliente: {nombre}")
        print(f"Documento: {documento}")
        print(f"Habitación: {habitacion} x {noches} noches - ${costo_habitacion:.2f}")
        if servicios_elegidos:
            print("Servicios adicionales:")
            for servicio in servicios_elegidos:
                print(f" - {servicio}: ${self.servicios[servicio]:.2f}")
        print(f"Total a pagar: ${costo_total:.2f}")
        print("------------------------")

# Función principal para correr el programa
def main():
    hotel = Hotel()
    while True:
        hotel.hacer_reserva()
        continuar = input("\n¿Desea hacer otra reserva? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()