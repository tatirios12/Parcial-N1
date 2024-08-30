from datetime import datetime

# Clase base Empleado
class Empleado:
    def __init__(self, nombre, anio_ingreso):
        self.nombre = nombre
        self.anio_ingreso = anio_ingreso
    
    def calcular_antiguedad(self):
        anio_actual = datetime.now().year
        return anio_actual - self.anio_ingreso
    
    def calcular_bono_antiguedad(self):
        antiguedad = self.calcular_antiguedad()
        if antiguedad > 5:
            return 100.00  # Bono fijo de $100.00
        else:
            return 0.00
    
    def calcular_salario(self):
        raise NotImplementedError("Esta función debe ser implementada en las subclases")

# Clase para empleados de plaza fija
class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, anio_ingreso, salario_base, comisiones):
        super().__init__(nombre, anio_ingreso)
        self.salario_base = salario_base
        self.comisiones = comisiones
    
    def calcular_salario(self):
        bono_antiguedad = self.calcular_bono_antiguedad()
        salario_total = self.salario_base + self.comisiones + bono_antiguedad
        return salario_total

# Clase para empleados por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, anio_ingreso, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, anio_ingreso)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas
    
    def calcular_salario(self):
        bono_antiguedad = self.calcular_bono_antiguedad()
        salario_total = (self.tarifa_hora * self.horas_trabajadas) + bono_antiguedad
        return salario_total

# Función para generar la planilla de pago
def generar_planilla(empleados):
    print("\n--- Planilla de Pago ---")
    for empleado in empleados:
        salario = empleado.calcular_salario()
        print(f"Empleado: {empleado.nombre} - Salario Total: ${salario:.2f}")

# Ejemplo de uso
empleados = [
    EmpleadoPlazaFija(nombre="Juan Pérez", anio_ingreso=2015, salario_base=1500.00, comisiones=300.00),
    EmpleadoPlazaFija(nombre="Ana Gómez", anio_ingreso=2010, salario_base=2000.00, comisiones=400.00),
    EmpleadoPorHoras(nombre="Carlos Ruiz", anio_ingreso=2018, tarifa_hora=15.00, horas_trabajadas=160),
    EmpleadoPorHoras(nombre="María López", anio_ingreso=2012, tarifa_hora=20.00, horas_trabajadas=120)
]

generar_planilla(empleados)