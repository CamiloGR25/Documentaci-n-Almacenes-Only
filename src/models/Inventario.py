class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                break

    def mostrar_inventario(self):
        for producto in self.productos:
            print(f"Codigo: {producto.codigo}, Nombre: {producto.nombre}, Descripcion: {producto.descripcion}, Cantidad: {producto.cantidad}, Costo: {producto.costo}")

