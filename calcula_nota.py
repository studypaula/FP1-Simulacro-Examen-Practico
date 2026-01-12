from datetime import date
from ejercicio1 import convierte_binario_a_decimal
from ejercicio2 import divide_cadena
from ejercicio3 import mayor_area
from ejercicio4 import calcula_racha_maxima
from ejercicio5 import es_matriz_identidad
from ejercicio6 import actualiza_stock
from ejercicio7 import calcula_precio_total_ultimos_dias, Producto
from ejercicio8 import categoria_mayor_gasto

results = {i: {"passed": 0, "total": 0, "fails": [], "cond": []} for i in range(1, 9)}

def expect(func, ex_num, msg="", cond=False):
    """
    Evalúa la expresión (pasada como lambda). 
    Si ocurre una excepción, se registra como fallo.
    Si devuelve False, se registra como fallo.
    Si devuelve True, suma un acierto.
    """
    if cond:
        results[ex_num]["cond"].append((func, msg))
        return

    results[ex_num]["total"] += 1
    try:
        ok = func()
    except Exception as e:
        results[ex_num]["fails"].append(f"{msg} -> Exception: {e}")
        return
        
    if ok:
        results[ex_num]["passed"] += 1
    else:
        results[ex_num]["fails"].append(f"{msg} -> False")

def process_conditionals():
    """
    Procesa las comprobaciones condicionales (si las hubiera).
    Solo se evalúan si todas las pruebas no condicionales del ejercicio han pasado.
    """
    for ex_num in range(1, 9):
        conds = results[ex_num]["cond"]
        if not conds:
            continue
        if results[ex_num]["passed"] == results[ex_num]["total"]:
            for func, msg in conds:
                results[ex_num]["total"] += 1
                try:
                    ok = func()
                except Exception as e:
                    results[ex_num]["fails"].append(f"{msg} -> Exception: {e}")
                    continue
                if ok:
                    results[ex_num]["passed"] += 1
                else:
                    results[ex_num]["fails"].append(f"{msg} -> False")

# ----------------------------------------------------------------------------
# DEFINICIÓN DE TESTS
# ----------------------------------------------------------------------------

def test_ejercicio01():
    expect(lambda: convierte_binario_a_decimal("0") == 0, 1, 'convierte_binario_a_decimal("0")')
    expect(lambda: convierte_binario_a_decimal("1") == 1, 1, 'convierte_binario_a_decimal("1")')
    expect(lambda: convierte_binario_a_decimal("10") == 2, 1, 'convierte_binario_a_decimal("10")')
    expect(lambda: convierte_binario_a_decimal("1010") == 10, 1, 'convierte_binario_a_decimal("1010")')
    expect(lambda: convierte_binario_a_decimal("1111") == 15, 1, 'convierte_binario_a_decimal("1111")')
    expect(lambda: convierte_binario_a_decimal("100000") == 32, 1, 'convierte_binario_a_decimal("100000")')
    expect(lambda: convierte_binario_a_decimal("110101") == 53, 1, 'convierte_binario_a_decimal("110101")')

def test_ejercicio02():
    expect(lambda: divide_cadena("abcdefghij") == ("acegi", "bdfhj"), 2, 'divide_cadena("abcdefghij")')
    expect(lambda: divide_cadena("1234567890") == ("13579", "24680"), 2, 'divide_cadena("1234567890")')
    expect(lambda: divide_cadena("a") == ("a", ""), 2, 'divide_cadena("a")')
    expect(lambda: divide_cadena("") == ("", ""), 2, 'divide_cadena("")')
    expect(lambda: divide_cadena("ab") == ("a", "b"), 2, 'divide_cadena("ab")')
    expect(lambda: divide_cadena("abcdef") == ("ace", "bdf"), 2, 'divide_cadena("abcdef")')

def test_ejercicio03():
    # Pruebas de funcionalidad básica
    expect(lambda: mayor_area([1,8,6,2,5,4,8,3,7]) == 49, 3, "mayor_area standard")
    expect(lambda: mayor_area([1,1]) == 1, 3, "mayor_area [1,1]")
    expect(lambda: mayor_area([4,3,2,1,4]) == 16, 3, "mayor_area extremos")
    expect(lambda: mayor_area([1,2,1]) == 2, 3, "mayor_area [1,2,1]")
    expect(lambda: mayor_area([1,2,4,3]) == 4, 3, "mayor_area [1,2,4,3]")
    expect(lambda: mayor_area([2,3,4,5,18,17,6]) == 17, 3, "mayor_area picos")
    expect(lambda: mayor_area([]) == 0, 3, "mayor_area vacio")
    expect(lambda: mayor_area([5]) == 0, 3, "mayor_area 1 elemento")
    
    # Prueba de no mutabilidad (side effect)
    alturas = [1,8,6,2,5,4,8,3,7]
    copia_alturas = alturas.copy()
    try:
        mayor_area(alturas)
        expect(lambda: alturas == copia_alturas, 3, "Lista original no modificada", cond=True)
    except Exception as e:
        results[3]["total"] += 1
        results[3]["fails"].append(f"Check mutabilidad -> Exception: {e}")

def test_ejercicio04():
    # Pruebas de funcionalidad
    expect(lambda: calcula_racha_maxima([]) == 0, 4, "racha vacia")
    expect(lambda: calcula_racha_maxima([date(2023,1,1)]) == 1, 4, "racha 1 elemento")
    expect(lambda: calcula_racha_maxima([date(2023,1,1), date(2023,1,2), date(2023,1,4), date(2023,1,5), date(2023,1,6)]) == 3, 4, "racha basica")
    expect(lambda: calcula_racha_maxima([date(2023,1,1), date(2023,1,2), date(2023,1,2), date(2023,1,4), date(2023,1,5), date(2023,1,6)]) == 3, 4, "racha con duplicados")
    expect(lambda: calcula_racha_maxima([date(2023,1,13), date(2023,1,11), date(2023,1,12), date(2023,1,10)]) == 4, 4, "racha desordenada")
    expect(lambda: calcula_racha_maxima([date(2023,1,1), date(2023,1,3), date(2023,1,5)]) == 1, 4, "racha alterna")
    expect(lambda: calcula_racha_maxima([date(2023,1,8), date(2023,1,6), date(2023,1,3), date(2023,1,2), date(2023,1,1)]) == 3, 4, "racha inversa parcial")
    expect(lambda: calcula_racha_maxima([date(2023,1,1), date(2023,1,2), date(2023,1,2), date(2023,1,3)]) == 3, 4, "racha duplicados consecutivos")

    # Prueba de no mutabilidad
    fechas = [date(2023,1,1), date(2023,1,2), date(2023,1,4), date(2023,1,5), date(2023,1,6)]
    copia_fechas = fechas.copy()
    try:
        calcula_racha_maxima(fechas)
        expect(lambda: fechas == copia_fechas, 4, "Lista fechas no modificada", cond=True)
    except Exception as e:
        results[4]["total"] += 1
        results[4]["fails"].append(f"Check mutabilidad -> Exception: {e}")

def test_ejercicio05():
    # Pruebas de funcionalidad
    expect(lambda: es_matriz_identidad([[1,0,0],[0,1,0],[0,0,1]]) == True, 5, "3x3 identidad")
    expect(lambda: es_matriz_identidad([[1,0],[0,1]]) == True, 5, "2x2 identidad")
    expect(lambda: es_matriz_identidad([[1]]) == True, 5, "1x1 identidad")
    expect(lambda: es_matriz_identidad([[0,0,0],[0,0,0],[0,0,0]]) == False, 5, "matriz ceros")
    expect(lambda: es_matriz_identidad([[1,0,0],[0,0,0],[0,0,1]]) == False, 5, "diagonal incompleta")
    expect(lambda: es_matriz_identidad([[1,2,0],[0,1,0],[0,0,1]]) == False, 5, "no ceros fuera diagonal")
    expect(lambda: es_matriz_identidad([[1,0,0],[0,1,0]]) == False, 5, "no cuadrada")
    expect(lambda: es_matriz_identidad([]) == False, 5, "vacia")

    # Prueba de no mutabilidad
    matriz = [[1,0,0],[0,1,0],[0,0,1]]
    copia_matriz = [fila.copy() for fila in matriz]
    try:
        es_matriz_identidad(matriz)
        expect(lambda: matriz == copia_matriz, 5, "Matriz original no modificada", cond=True)
    except Exception as e:
        results[5]["total"] += 1
        results[5]["fails"].append(f"Check mutabilidad -> Exception: {e}")

def test_ejercicio06():
    # Helper para ejecutar pruebas de stock de forma segura
    def run_stock_test(ventas_in, stock_in, expected_stock, expected_dev, case_name):
        try:
            # Copia profunda manual simple para el test si fuera necesaria, 
            # pero aquí pasamos literales nuevos en cada llamada.
            res_dev = actualiza_stock(ventas_in, stock_in)
            expect(lambda: stock_in == expected_stock, 6, f"{case_name} (stock)")
            expect(lambda: res_dev == expected_dev, 6, f"{case_name} (no_vendidas)")
        except Exception as e:
            results[6]["total"] += 2
            results[6]["fails"].append(f"{case_name} -> Exception: {e}")

    # Caso 1: Venta exacta
    run_stock_test([("Zumo", 1)], {"Zumo": 1}, {"Zumo": 0}, [], "Venta exacta")

    # Caso 2: Falta stock
    run_stock_test([("Galletas", 10)], {"Galletas": 5}, {"Galletas": 0}, [("Galletas", 5)], "Stock insuficiente")

    # Caso 3: Múltiples productos
    run_stock_test(
        [("Manzana", 5), ("Pan", 3), ("Leche", 2)],
        {"Manzana": 4, "Pan": 5, "Leche": 1},
        {"Manzana": 0, "Pan": 2, "Leche": 0},
        [("Manzana", 1), ("Leche", 1)],
        "Multiple mix"
    )

    # Caso 4: Stock no afectado (Huevos)
    run_stock_test(
        [("Manzana", 5), ("Pan", 3), ("Leche", 2)],
        {"Manzana": 4, "Pan": 5, "Leche": 1, "Huevos": 10},
        {"Manzana": 0, "Pan": 2, "Leche": 0, "Huevos": 10},
        [("Manzana", 1), ("Leche", 1)],
        "Item no tocado"
    )

    # Caso 5: Venta con stock 0 inicial
    run_stock_test(
        [("Arroz", 2), ("Frijoles", 1)],
        {"Arroz": 5, "Frijoles": 0},
        {"Arroz": 3, "Frijoles": 0},
        [("Frijoles", 1)],
        "Stock cero inicial"
    )

    # Caso 6: No mutabilidad de lista ventas
    ventas = [("Manzana", 5), ("Pan", 3), ("Leche", 2)]
    copia_ventas = ventas.copy()
    stock = {"Manzana": 4, "Pan": 5, "Leche": 1}
    try:
        actualiza_stock(ventas, stock)
        expect(lambda: ventas == copia_ventas, 6, "Lista ventas no modificada", cond=True)
    except Exception as e:
        results[6]["total"] += 1
        results[6]["fails"].append(f"Check mutabilidad -> Exception: {e}")

def test_ejercicio07():
    productos = [
        Producto("Leche", "Lácteos", 1.5, date(2024, 6, 20)),
        Producto("Pan", "Panadería", 1.0, date(2024, 6, 18)),
        Producto("Queso", "Lácteos", 3.0, date(2024, 6, 15)),
        Producto("Manzanas", "Frutas", 2.5, date(2024, 6, 10)),
    ]
    fecha_actual = date(2024, 6, 21)

    # Pruebas de cálculo
    expect(lambda: calcula_precio_total_ultimos_dias(productos, 2, fecha_actual) == 1.5, 7, "dias=2")
    expect(lambda: calcula_precio_total_ultimos_dias(productos, 4, fecha_actual) == 2.5, 7, "dias=4")
    expect(lambda: calcula_precio_total_ultimos_dias(productos, 9, fecha_actual) == 5.5, 7, "dias=9")
    expect(lambda: calcula_precio_total_ultimos_dias(productos, 14, fecha_actual) == 8, 7, "dias=14")
    expect(lambda: calcula_precio_total_ultimos_dias([], 6, fecha_actual) == 0.0, 7, "lista vacia")
    expect(lambda: calcula_precio_total_ultimos_dias(productos, 0, fecha_actual) == 0, 7, "dias=0")

    # Prueba de no mutabilidad
    copia_productos = productos.copy()
    try:
        calcula_precio_total_ultimos_dias(productos, 7, fecha_actual)
        expect(lambda: productos == copia_productos, 7, "Lista productos no modificada", cond=True)
    except Exception as e:
        results[7]["total"] += 1
        results[7]["fails"].append(f"Check mutabilidad -> Exception: {e}")

def test_ejercicio08():
    productos = [
        Producto("Leche", "Lácteos", 1.5, date(2024, 6, 20)),
        Producto("Pan", "Panadería", 1.0, date(2024, 6, 18)),
        Producto("Queso", "Lácteos", 3.0, date(2024, 6, 15)),
        Producto("Manzanas", "Frutas", 2.5, date(2024, 6, 10)),
    ]
    expect(lambda: categoria_mayor_gasto(productos) == ("Lácteos", 4.5), 8, "categoria mayor simple")
    expect(lambda: categoria_mayor_gasto([]) is None, 8, "lista vacia -> None", cond=True)

    productos2 = [
        Producto("Producto1", "Cat1", 10.0, date(2024, 1, 1)),
        Producto("Producto2", "Cat2", 20.0, date(2024, 1, 2)),
        Producto("Producto3", "Cat1", 15.0, date(2024, 1, 3)),
        Producto("Producto4", "Cat3", 5.0, date(2024, 1, 4)),
    ]
    expect(lambda: categoria_mayor_gasto(productos2) == ("Cat1", 25.0), 8, "categoria mayor acumulada")

    # Prueba de no mutabilidad
    copia_productos = productos.copy()
    try:
        categoria_mayor_gasto(productos)
        expect(lambda: productos == copia_productos, 8, "Lista productos no modificada", cond=True)
    except Exception as e:
        results[8]["total"] += 1
        results[8]["fails"].append(f"Check mutabilidad -> Exception: {e}")

def round_quarter(x):
    return round(x * 4) / 4.0

# ----------------------------------------------------------------------------
# EJECUCIÓN
# ----------------------------------------------------------------------------

test_ejercicio01()
test_ejercicio02()
test_ejercicio03()
test_ejercicio04()
test_ejercicio05()
test_ejercicio06()
test_ejercicio07()
test_ejercicio08()

process_conditionals()

PUNTOS_POR_EJ = 1.25
notas = {}
nota_final = 0.0

print("Informe de resultados:")
print("-" * 40)
for i in range(1, 9):
    passed = results[i]["passed"]
    total = results[i]["total"]
    fails = results[i]["fails"]
    
    if total == 0:
        nota = 0.0
    else:
        raw = (passed / total) * PUNTOS_POR_EJ
        nota = round_quarter(raw)
        
    notas[i] = nota
    nota_final += nota
    
    print(f"Ejercicio {i}: {passed}/{total} aciertos -> Nota: {nota:.2f}")
    if fails:
        for f in fails:
            print(f"  [X] {f}")
print("-" * 40)
print(f"Nota final: {nota_final:.2f} / {PUNTOS_POR_EJ * 8:.2f}")