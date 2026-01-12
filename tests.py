from datetime import date
from ejercicio1 import convierte_binario_a_decimal
from ejercicio2 import divide_cadena
from ejercicio3 import mayor_area
from ejercicio4 import calcula_racha_maxima
from ejercicio5 import es_matriz_identidad
from ejercicio6 import actualiza_stock
from ejercicio7 import calcula_precio_total_ultimos_dias, Producto
from ejercicio8 import categoria_mayor_gasto

def test_convierte_binario_a_decimal():
    print("Probando convierte_binario_a_decimal...", flush=True, end="")
    assert convierte_binario_a_decimal("0") == 0
    assert convierte_binario_a_decimal("1") == 1
    assert convierte_binario_a_decimal("10") == 2
    assert convierte_binario_a_decimal("1010") == 10
    assert convierte_binario_a_decimal("1111") == 15
    assert convierte_binario_a_decimal("100000") == 32
    assert convierte_binario_a_decimal("110101") == 53
    print("OK", flush=True)

def test_divide_cadena():
    print("Probando divide_cadena...", flush=True, end="")
    assert divide_cadena("abcdefghij") == ("acegi", "bdfhj")
    assert divide_cadena("1234567890") == ("13579", "24680")
    assert divide_cadena("a") == ("a", "")
    assert divide_cadena("") == ("", "")
    assert divide_cadena("ab") == ("a", "b")
    assert divide_cadena("abcdef") == ("ace", "bdf")
    print("OK", flush=True)

def test_mayor_area():
    print("Probando mayor_area...", flush=True, end="")
    assert mayor_area([1,8,6,2,5,4,8,3,7]) == 49
    assert mayor_area([1,1]) == 1
    assert mayor_area([4,3,2,1,4]) == 16
    assert mayor_area([1,2,1]) == 2
    assert mayor_area([1,2,4,3]) == 4
    assert mayor_area([2,3,4,5,18,17,6]) == 17  
    assert mayor_area([]) == 0
    assert mayor_area([5]) == 0
    
    # Probamos que la función no modifique la lista recibida
    alturas = [1,8,6,2,5,4,8,3,7]
    copia_alturas = alturas.copy()
    mayor_area(alturas)
    assert alturas == copia_alturas

    print("OK", flush=True)

def test_calcula_racha_maxima():
    from datetime import date
    print("Probando calcula_racha_maxima...", flush=True, end="")
    assert calcula_racha_maxima([]) == 0
    assert calcula_racha_maxima([date(2023,1,1)]) == 1
    assert calcula_racha_maxima([date(2023,1,1), date(2023,1,2), date(2023,1,4), date(2023,1,5), date(2023,1,6)]) == 3
    assert calcula_racha_maxima([date(2023,1,1), date(2023,1,2), date(2023,1,2), date(2023,1,4), date(2023,1,5), date(2023,1,6)]) == 3
    assert calcula_racha_maxima([date(2023,1,13), date(2023,1,11), date(2023,1,12), date(2023,1,10)]) == 4
    assert calcula_racha_maxima([date(2023,1,1), date(2023,1,3), date(2023,1,5)]) == 1
    assert calcula_racha_maxima([date(2023,1,8), date(2023,1,6), date(2023,1,3), date(2023,1,2), date(2023,1,1)]) == 3
    assert calcula_racha_maxima([date(2023,1,1), date(2023,1,2), date(2023,1,2), date(2023,1,3)]) == 3    

    # Probamos que la función no modifique la lista recibida
    fechas = [date(2023,1,1), date(2023,1,2), date(2023,1,4), date(2023,1,5), date(2023,1,6)]
    copia_fechas = fechas.copy()
    calcula_racha_maxima(fechas)
    assert fechas == copia_fechas

    print("OK", flush=True)

def test_es_matriz_identidad():
    print("Probando es_matriz_identidad...", flush=True, end="")
    assert es_matriz_identidad([[1,0,0],[0,1,0],[0,0,1]]) == True
    assert es_matriz_identidad([[1,0],[0,1]]) == True
    assert es_matriz_identidad([[1]]) == True
    assert es_matriz_identidad([[0,0,0],[0,0,0],[0,0,0]]) == False
    assert es_matriz_identidad([[1,0,0],[0,0,0],[0,0,1]]) == False
    assert es_matriz_identidad([[1,2,0],[0,1,0],[0,0,1]]) == False
    assert es_matriz_identidad([[1,0,0],[0,1,0]]) == False
    assert es_matriz_identidad([]) == False   

    # Probamos que la función no modifique la lista recibida
    matriz = [[1,0,0],[0,1,0],[0,0,1]]
    copia_matriz = [fila.copy() for fila in matriz]
    es_matriz_identidad(matriz)
    assert matriz == copia_matriz

    print("OK", flush=True)

def test_actualiza_stock():
    print("Probando actualiza_stock...", flush=True, end="")

    ventas = [("Zumo", 1)]
    stock = {"Zumo": 1}
    no_vendidas = actualiza_stock(ventas, stock)
    assert stock == {"Zumo": 0}
    assert no_vendidas == []

    ventas = [("Galletas", 10)]
    stock = {"Galletas": 5}
    no_vendidas = actualiza_stock(ventas, stock)
    assert stock == {"Galletas": 0}
    assert no_vendidas == [("Galletas", 5)]

    ventas = [("Manzana", 5), ("Pan", 3), ("Leche", 2)]
    stock = {"Manzana": 4, "Pan": 5, "Leche": 1}
    no_vendidas = actualiza_stock(ventas, stock)
    assert stock == {"Manzana": 0, "Pan": 2, "Leche": 0}
    assert no_vendidas == [("Manzana", 1), ("Leche", 1)]

    ventas = [("Manzana", 5), ("Pan", 3), ("Leche", 2)]
    stock = {"Manzana": 4, "Pan": 5, "Leche": 1, "Huevos": 10}
    no_vendidas = actualiza_stock(ventas, stock)
    assert stock == {"Manzana": 0, "Pan": 2, "Leche": 0, "Huevos": 10}
    assert no_vendidas == [("Manzana", 1), ("Leche", 1)]

    ventas = [("Arroz", 2), ("Frijoles", 1)]
    stock = {"Arroz": 5}
    no_vendidas = actualiza_stock(ventas, stock)
    assert stock == {"Arroz": 3, "Frijoles": 0}
    assert no_vendidas == [("Frijoles", 1)]

    # Probamos que la función no modifique la lista recibida
    ventas = [("Manzana", 5), ("Pan", 3), ("Leche", 2)]
    copia_ventas = ventas.copy()
    stock = {"Manzana": 4, "Pan": 5, "Leche": 1}
    actualiza_stock(ventas, stock)
    assert ventas == copia_ventas

    print("OK", flush=True)

def test_calcula_precio_total_ultimos_dias():    
    print("Probando calcula_precio_total_ultimos_dias...", flush=True, end="")   

    productos = [
        Producto("Leche", "Lácteos", 1.5, date(2024, 6, 20)),
        Producto("Pan", "Panadería", 1.0, date(2024, 6, 18)),
        Producto("Queso", "Lácteos", 3.0, date(2024, 6, 15)),
        Producto("Manzanas", "Frutas", 2.5, date(2024, 6, 10)),
    ]
    fecha_actual = date(2024, 6, 21)

    assert calcula_precio_total_ultimos_dias(productos, 2, fecha_actual) == 1.5
    assert calcula_precio_total_ultimos_dias(productos, 4, fecha_actual) == 2.5
    assert calcula_precio_total_ultimos_dias(productos, 9, fecha_actual) == 5.5
    assert calcula_precio_total_ultimos_dias(productos, 14, fecha_actual) == 8
    assert calcula_precio_total_ultimos_dias([], 6, fecha_actual) == 0.0
    assert calcula_precio_total_ultimos_dias(productos, 0, fecha_actual) == 0

    # Probamos que la función no modifique la lista recibida
    copia_productos = productos.copy()
    calcula_precio_total_ultimos_dias(productos, 7, fecha_actual)
    assert productos == copia_productos
    
    print("OK", flush=True)

def test_categoria_mayor_gasto():
    print("Probando categoria_mayor_gasto...", flush=True, end="")   

    productos = [
        Producto("Leche", "Lácteos", 1.5, date(2024, 6, 20)),
        Producto("Pan", "Panadería", 1.0, date(2024, 6, 18)),
        Producto("Queso", "Lácteos", 3.0, date(2024, 6, 15)),
        Producto("Manzanas", "Frutas", 2.5, date(2024, 6, 10)),
    ]

    assert categoria_mayor_gasto(productos) == ("Lácteos", 4.5)
    assert categoria_mayor_gasto([]) is None

    productos = [
        Producto("Producto1", "Cat1", 10.0, date(2024, 1, 1)),
        Producto("Producto2", "Cat2", 20.0, date(2024, 1, 2)),
        Producto("Producto3", "Cat1", 15.0, date(2024, 1, 3)),
        Producto("Producto4", "Cat3", 5.0, date(2024, 1, 4)),
    ]
    assert categoria_mayor_gasto(productos) == ("Cat1", 25.0)

    # Probamos que la función no modifique la lista recibida
    copia_productos = productos.copy()
    categoria_mayor_gasto(productos)
    assert productos == copia_productos

    print("OK", flush=True)

###############################################
# Descomenta las pruebas que quieras ejecutar #
###############################################

test_convierte_binario_a_decimal()
test_divide_cadena()
#test_mayor_area()
#test_calcula_racha_maxima()
test_es_matriz_identidad()
test_actualiza_stock()
#test_calcula_precio_total_ultimos_dias()
#test_categoria_mayor_gasto()