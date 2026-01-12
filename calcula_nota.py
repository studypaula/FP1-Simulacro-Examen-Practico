from datetime import date
from ejercicio01 import calcula_mcm
from ejercicio02 import introduce_asteriscos
from ejercicio03 import divide_pesos
from ejercicio04 import calcula_gastos
from ejercicio05 import resta_matrices
from ejercicio06 import calcula_factura, Producto
from ejercicio07 import busca_producto_mas_caro
from ejercicio08 import calcula_top_categorias

# Result tracking
results = {i: {"passed": 0, "total": 0, "fails": [], "cond": []} for i in range(1, 9)}

def expect(func, ex_num, msg="", cond=False):
    """Evalúa la expresión (pasada como lambda). Si cond=True, se guarda para evaluación
    posterior y solo se puntuará si el resto de pruebas del ejercicio han pasado."""
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
    """Procesa las comprobaciones condicionales: solo se evalúan si todas las pruebas no condicionales
    del ejercicio han pasado."""
    for ex_num in range(1, 9):
        conds = results[ex_num]["cond"]
        if not conds:
            continue
        # Solo evaluar condicionales si todas las pruebas no-condicionales han pasado
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
        # Si no han pasado todas las no-condicionales, no se puntúan las condicionales (no se añaden a total ni fails)

def test_ejercicio01():    
    expect(lambda: calcula_mcm(4, 5) == 20, 1, "calcula_mcm(4,5) == 20")
    expect(lambda: calcula_mcm(6, 8) == 24, 1, "calcula_mcm(6,8) == 24")
    expect(lambda: calcula_mcm(7, 3) == 21, 1, "calcula_mcm(7,3) == 21")
    expect(lambda: calcula_mcm(18, 12) == 36, 1, "calcula_mcm(18,12) == 36")
    expect(lambda: calcula_mcm(1, 1) == 1, 1, "calcula_mcm(1,1) == 1")
    expect(lambda: calcula_mcm(0, 5) is None, 1, "calcula_mcm(0,5) is None", cond=True)
    expect(lambda: calcula_mcm(5, 0) is None, 1, "calcula_mcm(5,0) is None", cond=True)
    

def test_ejercicio02():    
    expect(lambda: introduce_asteriscos("abcdefghij", 4) == "abc*efg*ij", 2, 'introduce_asteriscos("abcdefghij",4)')
    expect(lambda: introduce_asteriscos("Hola Mundo", 3) == "Ho*a *un*o", 2, 'introduce_asteriscos("Hola Mundo",3)')
    expect(lambda: introduce_asteriscos("Python", 2) == "P*t*o*", 2, 'introduce_asteriscos("Python",2)')
    expect(lambda: introduce_asteriscos("Python", 1) == "******", 2, 'introduce_asteriscos("Python",1)')
    expect(lambda: introduce_asteriscos("Corta", 7) == "Corta", 2, 'introduce_asteriscos("Corta",7)')
    expect(lambda: introduce_asteriscos("", 5) == "", 2, 'introduce_asteriscos("",5)')
    expect(lambda: introduce_asteriscos("A", 1) == "*", 2, 'introduce_asteriscos("A",1)')
    

def test_ejercicio03():    
    pesos = [10.0, 20.0, 15.0, 5.0, 10.0]
    pesos_copia = pesos.copy()
    try:
        lista1, lista2 = divide_pesos(pesos)
        expect(lambda: pesos == pesos_copia, 3, "original list not modified")
        expect(lambda: abs(sum(lista1) - sum(lista2)) < 1e-9, 3, "sum(lista1) == sum(lista2)")
    except Exception as e:
        results[3]["total"] += 2
        results[3]["fails"].append(f"divide_pesos basic case -> Exception: {e}")

    pesos = [12.5, 7.5, 10.0, 4.0]
    try:
        lista1, lista2 = divide_pesos(pesos)
        expect(lambda: abs(sum(lista1) - sum(lista2)) == 1.0, 3, "difference == 1.0")
    except Exception as e:
        results[3]["total"] += 1
        results[3]["fails"].append(f"divide_pesos case2 -> Exception: {e}")

    pesos = [5.0]
    try:
        lista1, lista2 = divide_pesos(pesos)
        expect(lambda: abs(sum(lista1) - sum(lista2)) == 5.0, 3, "single element difference 5.0")
    except Exception as e:
        results[3]["total"] += 1
        results[3]["fails"].append(f"divide_pesos single -> Exception: {e}")

    pesos = []
    try:
        lista1, lista2 = divide_pesos(pesos)
        expect(lambda: lista1 == [] and lista2 == [], 3, "empty lists")
    except Exception as e:
        results[3]["total"] += 1
        results[3]["fails"].append(f"divide_pesos empty -> Exception: {e}")

    

def test_ejercicio04():    
    gasto_diario = [10.0, 12.0, 11.0, 13.0, 12.5, 14.0, 15.0]
    fecha_inicio = date(2024, 6, 1)
    fecha_fin = date(2024, 6, 7)
    expect(lambda: calcula_gastos(gasto_diario, fecha_inicio, fecha_fin) == 87.5, 4, "gastos 1..7")

    fecha_inicio = date(2024, 6, 1)
    fecha_fin = date(2024, 6, 30)
    expect(lambda: calcula_gastos(gasto_diario, fecha_inicio, fecha_fin) == 379.0, 4, "gastos june full")

    fecha_inicio = date(2024, 6, 3)
    fecha_fin = date(2024, 6, 3)
    expect(lambda: calcula_gastos(gasto_diario, fecha_inicio, fecha_fin) == 10.0, 4, "same day")

    fecha_inicio = date(2024, 6, 3)
    fecha_fin = date(2024, 6, 2)
    expect(lambda: calcula_gastos(gasto_diario, fecha_inicio, fecha_fin) == 0.0, 4, "start after end -> 0.0")


def test_ejercicio05():
    mat1 = [[5, 8, 10],
            [4, 6, 9],
            [7, 3, 2]]

    mat2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    resultado_esperado = [[4, 6, 7],
                          [0, 1, 3],
                          [0, -5, -7]]

    expect(lambda: resta_matrices(mat1, mat2) == resultado_esperado, 5, "resta_matrices equal")

    mat3 = [[1, 2],
            [3, 4]]

    expect(lambda: resta_matrices(mat1, mat3) is None, 5, "incompatible sizes -> None", cond=True)

    expect(lambda: resta_matrices([], []) == [], 5, "empty matrices -> []")

def test_ejercicio06():
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
    try:
        factura = calcula_factura(productos, iva_por_categoria)
        expect(lambda: abs(factura["Ropa"] - (20.0 * 1.10 + 30.0 * 1.10)) < 1e-6, 6, "Ropa factura")
        expect(lambda: abs(factura["Cultura"] - (15.0 * 1.04 + 25.0 * 1.04)) < 1e-6, 6, "Cultura factura")
        expect(lambda: abs(factura["Alimentos"] - (10.0 * 1.21)) < 1e-6, 6, "Alimentos factura")
    except Exception as e:
        # If calcula_factura raises, count the three expected checks as failed
        results[6]["total"] += 3
        results[6]["fails"].append(f"calcula_factura -> Exception: {e}")

def test_ejercicio07():
    productos = [
        Producto(nombre="Camisa", categoria="Ropa", precio=20.0),
        Producto(nombre="Pantalón", categoria="Ropa", precio=30.0),
        Producto(nombre="Libro", categoria="Cultura", precio=15.0),
        Producto(nombre="Película", categoria="Cultura", precio=25.0),
        Producto(nombre="Comida", categoria="Alimentos", precio=10.0)
    ]

    expect(lambda: busca_producto_mas_caro(productos) == Producto(nombre="Pantalón", categoria="Ropa", precio=30.0), 7, "most expensive overall")
    expect(lambda: busca_producto_mas_caro(productos, categoria="Cultura") == Producto(nombre="Película", categoria="Cultura", precio=25.0), 7, "most expensive Cultura")
    expect(lambda: busca_producto_mas_caro(productos, categoria="Alimentos") == Producto(nombre="Comida", categoria="Alimentos", precio=10.0), 7, "most expensive Alimentos")
    expect(lambda: busca_producto_mas_caro(productos, categoria="Electrónica") is None, 7, "non-existent category -> None", cond=True)
    expect(lambda: busca_producto_mas_caro([]) is None, 7, "empty list -> None", cond=True)

def test_ejercicio08():
    productos = [
        Producto(nombre="Camisa", categoria="Ropa", precio=20.0),
        Producto(nombre="Pantalón", categoria="Ropa", precio=30.0),
        Producto(nombre="Libro", categoria="Cultura", precio=15.0),
        Producto(nombre="Película", categoria="Cultura", precio=25.0),
        Producto(nombre="Comida", categoria="Alimentos", precio=10.0)
    ]
    expect(lambda: calcula_top_categorias(productos, n=2) == [("Ropa", 50.0), ("Cultura", 40.0)], 8, "top 2 categorias")
    expect(lambda: calcula_top_categorias(productos, n=3) == [("Ropa", 50.0), ("Cultura", 40.0), ("Alimentos", 10.0)], 8, "top 3 categorias")


def round_quarter(x):
    return round(x * 4) / 4.0

# Ejecutar pruebas
test_ejercicio01()
test_ejercicio02()
test_ejercicio03()
test_ejercicio04()
test_ejercicio05()
test_ejercicio06()
test_ejercicio07()
test_ejercicio08()

# Procesar comprobaciones condicionales (solo se puntúan si el resto pasó)
process_conditionals()

# Calcular notas
PUNTOS_POR_EJ = 1.25
notas = {}
nota_final = 0.0

print("Informe de resultados:")
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
    print(f"Ejercicio {i:02d}: {passed}/{total} aciertos, Nota: {nota:.2f}")
    if fails:
        # Mostrar solo los fallos para este ejercicio
        for f in fails:
            print(f"  - {f}")

print(f"\nNota final: {nota_final:.2f} / {PUNTOS_POR_EJ * 8:.2f}")