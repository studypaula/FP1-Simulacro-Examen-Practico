from collections import namedtuple, defaultdict

Producto = namedtuple('Producto', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio'        # tipo float
])

def calcula_top_categorias(productos: list[Producto], n: int = 3) -> list[tuple[str, float]]:
    """
    Calcula las N categorías con mayor precio total de productos y devuelve
    una lista ordenada de tuplas (categoría, valor_total).
    
    Parámetros:
    productos (list[Producto]): Lista de tuplas de tipo Producto.
    n (int): Número de categorías a devolver (por defecto 3).
    
    Devuelve:
    list[tuple[str, float]]: Lista con las N categorías de mayor valor total.
    """
    # TODO: Borra este comentario y la instrucción pass, e implementa la función
    pass