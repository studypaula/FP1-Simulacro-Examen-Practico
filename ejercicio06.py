from collections import namedtuple

Producto = namedtuple('Producto', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio'        # tipo float    
])

def calcula_factura(productos: list[Producto], iva_por_categoria: dict[str, float]) -> dict[str, float]:
    """ 
    Calcula el desglose de una factura por categorías, incluyendo para cada categoría el precio
    total de los productos de esa categoría una vez aplicado el IVA correspondiente.
    Si una categoría no está contemplada en el diccionario recibido, se asume un IVA del 21%.

    Parámetros:
    productos (list[Producto]): Lista de productos.
    iva_por_categoria (dict[str, float]): Diccionario con el IVA por categoría.

    Devuelve:
    dict[str, float]: Diccionario donde las claves son categorías de los productos recibidos y 
    los valores son el precio total con IVA aplicado para esa categoría.
    """
    # TODO: Borra este comentario y la instrucción pass, e implementa la función
    pass