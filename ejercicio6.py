def actualiza_stock(ventas: list[tuple[str, int]], stock: dict[str, int]) -> list[tuple[str, int]]:
    """
    Actualiza el stock de productos tras una serie de ventas. Cada venta viene representada por una tupla
    con el nombre del producto y la cantidad vendida. Si una venta intenta vender más unidades de las que hay en stock,
    se vende únicamente la cantidad disponible.

    Además de actualizar el diccionario stock, la función devuelve una lista de tuplas con los nombres de 
    los productos y las cantidades que no han podido ser vendidas por falta de stock.    

    Parámetros:
    ventas (list[tuple[str, int]]): Lista de ventas, cada una representada por una tupla (nombre_producto, cantidad_vendida).
    stock (dict[str, int]): Diccionario con el stock actual de productos.

    Devuelve:
    list[tuple[str, int]]: Lista de tuplas con los nombres de los productos y las cantidades no vendidas por falta de stock.
    """
    res = []
    productos_stock = [p for p in stock]
    for p in ventas:
        if p[0] not in productos_stock:
            res.append(p)
            stock[p[0]] =0
        elif (stock[p[0]] -p[1]) <0:
            res.append((p[0],-(stock[p[0]]-p[1])))
            stock[p[0]]-=(p[1]+(stock[p[0]]-p[1]))
        else:
            stock[p[0]]-=p[1]    
    return res        