def mayor_area(alturas: list[int]) -> int:
    '''
    Dada una lista de alturas que representan paredes verticales en un plano cartesiano,
    encuentra la mayor área que se puede formar entre dos paredes y el eje x. Téngase
    en cuenta que el área está limitada por la pared más baja de las dos escogidas.
    
    Parámetros:
    alturas (list[int]): Lista de alturas de las paredes.

    Devuelve:
    int: La mayor área posible entre dos paredes.
    '''
    alturas2 = alturas.sort(reverse=True)
    for i, j in zip(alturas, alturas2):
        area = min(i,j)*(alturas)