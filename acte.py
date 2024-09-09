class EquipoDeportivo:
    def __init__(self, fecha_creacion, precio_costo, precio_venta, descripcion, cantidad_stock):
        self.fecha_creacion = fecha_creacion
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.descripcion = descripcion
        self.cantidad_stock = cantidad_stock

    def vender(self, cantidad_vendida):
        if cantidad_vendida > self.cantidad_stock:
            print("No hay suficiente stock para realizar la venta.")
            return False
        else:
            self.cantidad_stock -= cantidad_vendida
            return True

    def mostrar_info(self):
        return (f"Descripción: {self.descripcion}, Fecha de creación: {self.fecha_creacion}, "
                f"Precio costo: {self.precio_costo}, Precio venta: {self.precio_venta}, "
                f"Cantidad en stock: {self.cantidad_stock}")


# Función para manejar las ventas
def realizar_venta(equipo, cantidad):
    cantidad_original = equipo.cantidad_stock
    if equipo.vender(cantidad):
        print(f"Venta realizada. Cantidad original: {cantidad_original}, "
              f"Cantidad después de la venta: {equipo.cantidad_stock}")
    else:
        print("Venta no realizada.")


# Ejemplo de uso
if __name__ == "__main__":
    # Creación de objetos de equipos deportivos
    balon_futbol = EquipoDeportivo("2023-05-01", 20.0, 30.0, "Balón de fútbol", 100)
    raqueta_tenis = EquipoDeportivo("2023-06-15", 50.0, 75.0, "Raqueta de tenis", 50)

    # Mostrar información inicial
    print(balon_futbol.mostrar_info())
    print(raqueta_tenis.mostrar_info())

    # Realizar algunas ventas
    realizar_venta(balon_futbol, 10)
    realizar_venta(raqueta_tenis, 5)

    # Mostrar información después de las ventas
    print(balon_futbol.mostrar_info())
    print(raqueta_tenis.mostrar_info())

    # Intentar vender más de lo que hay en stock
    realizar_venta(balon_futbol, 95)  # Esto debería fallar