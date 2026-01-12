from collections import namedtuple
from datetime import date, timedelta

Producto = namedtuple('Producto', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio',       # tipo float
    'fecha_compra'  # tipo date
])

def calcula_precio_total_ultimos_dias(productos: list[Producto], dias: int, fecha_actual: date) -> float:
    """
    Calcula el precio total de los productos comprados en los últimos 'dias' días.
    Por ejemplo, si dias=7, se suman los precios de los productos comprados en los últimos 7 días
    anteriores a la fecha_actual.

    Parámetros:
    productos (list[Producto]): Lista de productos.
    dias (int): Número de días hacia atrás desde la fecha actual.
    fecha_actual (date): La fecha actual para comparar.

    Devuelve:
    float: El precio total de los productos comprados en los últimos 'dias' días.
    """
    