import csv
from datetime import datetime

# Función para registrar la asistencia de un estudiante
def registrar_asistencia(estudiante, estado, razon=None):
    fecha = datetime.now().strftime("%Y-%m-%d")
    with open('asistencia.csv', mode='a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([fecha, estudiante, estado, razon])

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nMenu de Asistencia")
    print("1. Registrar Asistencia")
    print("2. Registrar Inasistencia")
    print("3. Registrar Permiso")
    print("4. Salir")
    return input("Selecciona una opción: ")

# Función principal
def main():
    estudiantes = ['Juan Perez', 'Maria Lopez', 'Carlos Gomez']  # Lista de estudiantes
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1' or opcion == '2':
            estado = 'Asistencia' if opcion == '1' else 'Inasistencia'
            for i, estudiante in enumerate(estudiantes):
                print(f"{i + 1}. {estudiante}")
            seleccion = int(input("Selecciona el estudiante: ")) - 1
            registrar_asistencia(estudiantes[seleccion], estado)
            print(f"{estado} registrada para {estudiantes[seleccion]}")
        
        elif opcion == '3':
            for i, estudiante in enumerate(estudiantes):
                print(f"{i + 1}. {estudiante}")
            seleccion = int(input("Selecciona el estudiante: ")) - 1
            razon = input("Ingresa la razón del permiso: ")
            registrar_asistencia(estudiantes[seleccion], 'Permiso', razon)
            print(f"Permiso registrado para {estudiantes[seleccion]} con razón: {razon}")
        
        elif opcion == '4':
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()