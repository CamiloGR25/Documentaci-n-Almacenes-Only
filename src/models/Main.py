from Inventario import Inventario
from Producto import Producto

class Main:
    @staticmethod
    def Pruebas():
        # Crear un nuevo producto
        producto1 = Producto("P001", "Camiseta talla M", "Camiseta marca Nike talla M", 50, 30000)

        # Crear un nuevo inventario y agregar el producto
        inventario = Inventario()
        inventario.agregar_producto(producto1)

        # Mostrar el inventario
        inventario.mostrar_inventario()

        # Eliminar un producto por su código
        inventario.eliminar_producto("P001")

        # Mostrar el inventario después de eliminar
        inventario.mostrar_inventario()

# Ejecutar pruebas
if __name__ == "__main__":
    Main.Pruebas()