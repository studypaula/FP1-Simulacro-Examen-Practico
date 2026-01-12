from collections import namedtuple
from collections import defaultdict

Producto = namedtuple('Producto', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio',       # tipo float
    'fecha_compra'  # tipo date
])

def categoria_mayor_gasto(productos: list[Producto]) -> tuple[str, float] | None:
    """
    Determina la categoría con el mayor gasto total. Devuelve el nombre de la categoría
    junto con el gasto total en esa categoría.

    Si la lista de productos está vacía, devuelve None.

    Parámetros:
    productos (list[Producto]): Lista de productos.

    Devuelve:
    tuple[str, float] | None: La categoría con el mayor gasto total y el gasto total, o None si la lista de productos está vacía.
    """
    categoria_precios = defaultdict(list)
    if productos==[]:
        return None
    categoria_precio_max = {}
    categorias= [p.categoria for p in productos]
    for c in categorias:
        for p in productos:
            if p.categoria == c:
                categoria_precios[c].append((p.precio, p))
        categoria_precio_max =         
                
        



