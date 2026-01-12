from datetime import date
from ejercicio01 import calcula_mcm
from ejercicio02 import introduce_asteriscos
from ejercicio03 import divide_pesos
from ejercicio04 import calcula_gastos
from ejercicio05 import resta_matrices
from ejercicio06 import calcula_factura, Producto
from ejercicio07 import busca_producto_mas_caro
from ejercicio08 import calcula_top_categorias

def test_ejercicio01():
    print("Probando calcula_mcm...", end="")
    assert calcula_mcm(4, 5) == 20
    assert calcula_mcm(6, 8) == 24
    assert calcula_mcm(7, 3) == 21
    assert calcula_mcm(18, 12) == 36
    assert calcula_mcm(1, 1) == 1
    assert calcula_mcm(0, 5) == None
    assert calcula_mcm(5, 0) == None
    print(" OK")

def test_ejercicio02():
    print("Probando introduce_asteriscos...", end="")
    assert introduce_asteriscos("abcdefghij", 4) == "abc*efg*ij"
    assert introduce_asteriscos("Hola Mundo", 3) == "Ho*a *un*o"
    assert introduce_asteriscos("Python", 2) == "P*t*o*"
    assert introduce_asteriscos("Python", 1) == "******"
    assert introduce_asteriscos("Corta", 7) == "Corta"
    assert introduce_asteriscos("", 5) == ""
    assert introduce_asteriscos("A", 1) == "*"
    print(" OK")

def test_ejercicio03():
    print("Probando divide_pesos...", end="")
    pesos = [10.0, 20.0, 15.0, 5.0, 10.0]
    pesos_copia = pesos.copy()
    lista1, lista2 = divide_pesos(pesos)
    assert pesos == pesos_copia # Verifica que la lista original no se modifique
    assert sum(lista1) == sum(lista2)

    pesos = [12.5, 7.5, 10.0, 4.0]
    lista1, lista2 = divide_pesos(pesos)    
    assert abs(sum(lista1) - sum(lista2)) == 1.0

    pesos = [5.0]
    lista1, lista2 = divide_pesos(pesos)
    assert abs(sum(lista1) - sum(lista2)) == 5.0

    pesos = []
    lista1, lista2 = divide_pesos(pesos)
    assert lista1 == [] and lista2 == []
    print(" OK")

def test_ejercicio04():
    print("Probando calcula_gastos...", end="")
    from datetime import date

    gasto_diario = [10.0, 12.0, 11.0, 13.0, 12.5, 14.0, 15.0]
    fecha_inicio = date(2024, 6, 1)
    fecha_fin = date(2024, 6, 7)
    assert calcula_gastos(gasto_diario, fecha_inicio, fecha_fin) == 87.5

    fecha_inicio = date(2024, 6, 1)
    fecha_fin = date(2024, 6, 30)
    assert calcula_gastos(gasto_diario, fecha_inicio, fecha_fin) == 379.0

    fecha_inicio = date(2024, 6, 3)
    fecha_fin = date(2024, 6, 3)
    assert calcula_gastos(gasto_diario, fecha_inicio, fecha_fin) == 10.0

    fecha_inicio = date(2024, 6, 3)
    fecha_fin = date(2024, 6, 2)
    assert calcula_gastos(gasto_diario, fecha_inicio, fecha_fin) == 0.0 # Fecha inicio después de fecha fin

    print(" OK")

def test_ejercicio05():
    print("Probando resta_matrices...", end="")
    mat1 = [[5, 8, 10],
            [4, 6, 9],
            [7, 3, 2]]

    mat2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    resultado_esperado = [[4, 6, 7],
                          [0, 1, 3],
                          [0, -5, -7]]
    
    assert resta_matrices(mat1, mat2) == resultado_esperado

    mat3 = [[1, 2],
            [3, 4]]
    
    assert resta_matrices(mat1, mat3) == None

    assert resta_matrices([], []) == [] # La suma de dos matrices vacias es una matriz vacía
    print(" OK")

def test_ejercicio06():    
    print("Probando calcula_factura...", end="")
    productos = [
        Producto(nombre="Camisa", categoria="Ropa", precio=20.0),
        Producto(nombre="Pantalón", categoria="Ropa", precio=30.0),
        Producto(nombre="Libro", categoria="Cultura", precio=15.0),
        Producto(nombre="Película", categoria="Cultura", precio=25.0),
        Producto(nombre="Comida", categoria="Alimentos", precio=10.0)
    ]
    iva_por_categoria = {
        "Ropa": 0.10,
        "Cultura": 0.04
    }
    factura = calcula_factura(productos, iva_por_categoria)
    
    assert abs(factura["Ropa"] - (20.0 * 1.10 + 30.0 * 1.10)) < 1e-6
    assert abs(factura["Cultura"] - (15.0 * 1.04 + 25.0 * 1.04)) < 1e-6
    assert abs(factura["Alimentos"] - (10.0 * 1.21)) < 1e-6
    print(" OK")
    
def test_ejercicio07():    
    print("Probando busca_producto_mas_caro...", end="")
    productos = [
        Producto(nombre="Camisa", categoria="Ropa", precio=20.0),
        Producto(nombre="Pantalón", categoria="Ropa", precio=30.0),
        Producto(nombre="Libro", categoria="Cultura", precio=15.0),
        Producto(nombre="Película", categoria="Cultura", precio=25.0),
        Producto(nombre="Comida", categoria="Alimentos", precio=10.0)
    ]

    producto_mas_caro = busca_producto_mas_caro(productos)
    assert producto_mas_caro == Producto(nombre="Pantalón", categoria="Ropa", precio=30.0)

    producto_mas_caro_ropa = busca_producto_mas_caro(productos, categoria="Cultura")
    assert producto_mas_caro_ropa == Producto(nombre="Película", categoria="Cultura", precio=25.0)

    producto_mas_caro_ropa = busca_producto_mas_caro(productos, categoria="Alimentos")
    assert producto_mas_caro_ropa == Producto(nombre="Comida", categoria="Alimentos", precio=10.0)

    producto_no_existente = busca_producto_mas_caro(productos, categoria="Electrónica")
    assert producto_no_existente == None

    productos_vacios = []
    assert busca_producto_mas_caro(productos_vacios) == None
    print(" OK")

def test_ejercicio08():    
    print("Probando calcula_top_categorias...", end="")
    productos = [
        Producto(nombre="Camisa", categoria="Ropa", precio=20.0),
        Producto(nombre="Pantalón", categoria="Ropa", precio=30.0),
        Producto(nombre="Libro", categoria="Cultura", precio=15.0),
        Producto(nombre="Película", categoria="Cultura", precio=25.0),
        Producto(nombre="Comida", categoria="Alimentos", precio=10.0)
    ]
    top_categorias = calcula_top_categorias(productos, n=2)
    assert top_categorias == [("Ropa", 50.0), ("Cultura", 40.0)]

    top_categorias = calcula_top_categorias(productos, n=3)
    assert top_categorias == [("Ropa", 50.0), ("Cultura", 40.0), ("Alimentos", 10.0)]

    print(" OK")


test_ejercicio01()
test_ejercicio02()
test_ejercicio03()
test_ejercicio04()
test_ejercicio05()
test_ejercicio06()
test_ejercicio07()
test_ejercicio08()
print("Todos los tests pasaron correctamente.")