def divide_cadena(texto: str) -> tuple[str, str]:
    """
    Divide la cadena en dos, una fomada por los caracteres
    pares y otra por los impares.

    Parámetros:
    texto (str): El texto original.

    Devuelve:
    tuple[str, str]: Una tupla con dos cadenas, la primera con los caracteres en posiciones pares
                     y la segunda con los caracteres en posiciones impares.
    """
    cadena1 = ""
    cadena2 = ""
    for pos, i in enumerate(texto):
        if pos==0:
            cadena1 += i
        elif pos%2==0:
            cadena1 += i
        else:
            cadena2 += i
    return (cadena1, cadena2)            
