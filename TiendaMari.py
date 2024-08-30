class Tienda:
    def __init__(self):
        # Diccionario para almacenar los productos en inventario
        # La clave es el nombre del producto y el valor es un diccionario con 'cantidad' y 'precio'
        self.inventario = {}
        self.ventas = []

    def agregar_producto(self, nombre, cantidad, precio):
        if nombre in self.inventario:
            # Si el producto ya está en el inventario, se actualiza la cantidad
            self.inventario[nombre]['cantidad'] += cantidad
            self.inventario[nombre]['precio'] = precio
        else:
            # Si es un producto nuevo, se añade al inventario
            self.inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        print(f"Producto {nombre} agregado/actualizado. Cantidad: {cantidad}, Precio: {precio}")

    def registrar_venta(self, productos_vendidos):
        total = 0
        for nombre, cantidad in productos_vendidos.items():
            if nombre in self.inventario and self.inventario[nombre]['cantidad'] >= cantidad:
                precio_producto = self.inventario[nombre]['precio']
                total += precio_producto * cantidad
                self.inventario[nombre]['cantidad'] -= cantidad
                print(f"Venta registrada: {cantidad} de {nombre} a {precio_producto} cada uno.")
            else:
                print(f"No hay suficiente inventario para {nombre}.")
        self.ventas.append({'productos': productos_vendidos, 'total': total})
        return total

    def calcular_vuelto(self, total, pago):
        if pago >= total:
            return pago - total
        else:
            print("Pago insuficiente.")
            return None

    def mostrar_inventario(self):
        print("Inventario actual:")
        for nombre, datos in self.inventario.items():
            print(f"Producto: {nombre}, Cantidad: {datos['cantidad']}, Precio: {datos['precio']}")

    def mostrar_ventas(self):
        print("Historial de ventas:")
        for venta in self.ventas:
            print(f"Productos vendidos: {venta['productos']}, Total: {venta['total']}")

# Ejemplo de uso
tienda = Tienda()

# Niña Mary agrega productos al inventario
tienda.agregar_producto("Manzanas", 50, 0.5)
tienda.agregar_producto("Leche", 30, 1.2)

# Niña Mary registra una venta
total_venta = tienda.registrar_venta({"Manzanas": 5, "Leche": 2})

# Niña Mary calcula el vuelto
pago_cliente = 10  # El cliente paga 10
vuelto = tienda.calcular_vuelto(total_venta, pago_cliente)
print(f"El vuelto para el cliente es: {vuelto}")

# Mostrar inventario y ventas
tienda.mostrar_inventario()
tienda.mostrar_ventas()