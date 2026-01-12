def es_matriz_identidad(mat: list[list[int]]) -> bool:
    """
    Comprueba si una matriz es la matriz identidad. Una matriz 
    identidad es una matriz cuadrada en la que todos los elementos
    de la diagonal principal son 1 y el resto son 0.    

    Parámetros:
    mat (list[list[int]]): Matriz a comprobar.

    Devuelve:
    bool: True si la matriz es una matriz identidad, False en caso contrario.
    """
    if mat ==[]:
        return False
    if len(mat) != len(mat[0]):
        return False
    for i in range(len(mat)-1):
        for j in range(len(mat)-1):
            if i == j:
                if mat[i][j] != 1:
                    return False
            else:
                if mat[i][j] != 0:
                    return False
    return True        
    
    
