from datetime import date
from datetime import timedelta

def calcula_racha_maxima(fechas: list[date]) -> int:
    '''
    Dada una lista de fechas, calcula la racha máxima de días consecutivos.
    
    La lista de fechas puede no estar ordenadas y puede contener duplicados, los cuáles
    no serán tenidos en cuenta para el cálculo de las rachas.

    Parámetros:
    fechas (list[date]): Lista de fechas.

    Devuelve:
    int: La racha máxima de días consecutivos.  
    '''
    if fechas == []:
        return 0
    fechas_filtro = set(fechas)
    fecha_orden_filtro = sorted(fechas_filtro)
    racha = 1
    racha_maxima = 1
    if len(fecha_orden_filtro)==1:
        return racha_maxima
    for i, j in zip(fecha_orden_filtro, fecha_orden_filtro):
            if (i-j) == timedelta(days=1):
                racha += 1
                if racha > racha_maxima:
                    racha_maxima =  racha 
            else:
                racha = 1
    return racha_maxima        
               
