def convierte_binario_a_decimal(binario: str) -> int:
    """
    Convierte un número binario (representado como cadena) a su 
    representación decimal (como número entero).
    
    Por ejemplo, "1010" se convierte a 10.

    Parámetros:
    binario (str): Número binario como cadena.

    Devuelve:
    int: El número decimal correspondiente.
    """
    res = 0
    for pos, numero in enumerate(binario):
        numero1 = int(numero)
        if numero1==1:
            res += 2**(len(binario)-(pos+1))
    return res        


