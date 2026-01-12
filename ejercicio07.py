from collections import namedtuple, defaultdict

Producto = namedtuple('Producto', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio'        # tipo float
])

def busca_producto_mas_caro(productos: list[Producto], categoria: str | None = None) -> Producto | None:
    """
    Busca el producto más caro de una categoría específica.

    Parámetros:
    productos (list[Producto]): Lista de productos.
    categoria (str | None): La categoría a buscar. Si es None, se busca entre todos los productos.

    Devuelve:
    Producto | None: El producto más caro en la categoría dada, o None si no hay productos en esa categoría.
    """
    # TODO: Borra este comentario y la instrucción pass, e implementa la función
    pass