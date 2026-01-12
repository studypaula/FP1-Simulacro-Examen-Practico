# Examen práctico (Simulacro)
## Fundamentos de Programación 1. Grado en Ingeniería Informática – Inteligencia Artificial (Universidad de Sevilla)

## Instrucciones

1. Completa tu **nombre y apellidos** en el fichero `identificacion.txt`.
2. Activa la opción **Autoguardado (Auto Save)** en el menú Archivo (File).
3. Realiza cada ejercicio número XX en el módulo `src/ejercicioXX.py`. **No toques los prototipos de las funciones ni los comentarios de documentación**.
4. Asegúrate de comprobar que tu implementación pasa todos los tests. Para ejecutar los tests del ejercicio número XX, descomenta la línea `#test_ejercicioXX()` que encontrarás al final del módulo `src/tests.py` y ejecútalo. 
5. Si algún test falla, **utiliza el depurador para tratar de solucionarlo**. 
6. Puedes ejecutar el módulo `src/calcula_nota.py` para obtener una estimación de tu nota. Ten en cuenta que se trata de una nota aproximada, ya que:
   * La nota de un ejercicio puede ser más baja, si la implementación comete errores no detectados por los tests automáticos.
   * La nota de un ejercicio puede ser más alta, si se han cometido errores menores que han impedido pasar algunos tests automáticos.

## Ejercicios

### Ejercicio 1 (1,25 puntos)

Implementa la función `calcula_mcm`, que recibe dos números enteros positivos (**a** y **b**) y devuelve el mínimo común múltiplo (mcm). El mcm es el número más bajo que cumple ser múltiplo de ambos números, excluyendo el 0. Por ejemplo, el mcm de 2 y 3 es el 6.

Si la función recibiera algún número menor o igual a 0, debe devolver `None`.

Un posible algoritmo para resolverlo es el siguiente:
1. Nuestro primer **candidato** es **b**.
2. Si el **candidato** es múltiplo de **a**, el **candidato** es el mcm.
3. Si no, sumamos al **candidato** el valor de **b**, y volvemos al punto 2.

---

### Ejercicio 2 (1,25 puntos)

Implementa la función `introduce_asteriscos`, que recibe un **texto** y un entero **multiplos_de** y devuelve el texto susituyendo algunos caracteres por asteriscos. Los caracteres a sustituir serán aquellos que estén en posiciones múltiplos del número indicado por el parámetro, entendiendo que el primer carácter es el que está en la posición 1.
    
Por ejemplo, si el **texto** es `"abcdefghij"` y **multiplos_de** es `4`, el resultado devuelto será `"abc*efg*ij"`.

---

### Ejercicio 3 (1,25 puntos)

Implementa la función `divide_pesos`, que recibe una lista de números reales **pesos** y los divide en dos listas, de manera que los pesos de las dos listas obtenidas sean lo más equilibrados posible.

La función **no debe modificar la lista recibida**, sino que creará dos nuevas listas que serán devueltas.

Para ello, sigue este algoritmo:
1. Obtén una versión ordenada de la lista de **pesos** original, de mayor a menor.
2. Recorre la lista ordenada y añade cada peso a la lista que en cada momento tenga menor peso total.        

Por ejemplo, si la lista de **pesos** es:
```python
[12.5, 7.5, 10.0, 4.0]
```

la función podría devolver estas dos listas:
```python
([12.5,4.0], [10.0, 7.5])
```

---

### Ejercicio 4 (1,25 puntos)

Implementa una función `calcula_gastos`, que calcula el gasto total entre una **fecha_inicio** y una **fecha_fin**, sumando el gasto de cada día. La función recibe una lista **gasto_diario** que contiene el gasto diario según el día de la semana. La lista tiene por tanto siete posiciones: 0=lunes, 1=martes, ..., 6=domingo. **No es necesario comprobar que la lista gasto_diario tiene el número de elementos esperado**.

Por ejemplo, si **gasto_diario** es `[10.0, 12.0, 11.0, 13.0, 12.5, 14.0, 15.0]`, la **fecha_inicio** es `date(2024, 6, 1)` y la **fecha_fin** es `date(2024, 6, 7)`, la función calcula esta suma:

* 1 de junio de 2024 (sábado) => suma 14.0
* 2 de junio de 2024 (domingo) => suma 15.0
* 3 de junio de 2024 (lunes) => suma 10.0
* 4 de junio de 2024 (martes) => suma 12.0
* 5 de junio de 2024 (miércoles) => suma 11.0
* 6 de junio de 2024 (jueves) => suma 13.0
* 7 de junio de 2024 (viernes) => suma 12.5

La función devolvería el gasto total, que es `87.5`.

Puedes resolverlo iterando sobre las fechas, comenzando en la **fecha_inicio** y sumando un día en cada iteración hasta llegar a la **fecha_fin**.

---

### Ejercicio 5 (1,25 puntos)

Implementa la función  `resta_matrices` que recibe dos matrices numéricas del mismo tamaño (mismas filas y mismas columnas) y devuelve el resultado de restarlas. Para restar dos matrices, hay que restar las posiciones iguales de cada matriz. 

Si las matrices recibidas no tuvieran el mismo tamaño, la función devolvería `None`.

Por ejemplo, si las matrices son:
```python
mat1 = [[5, 8, 10],
        [4, 6, 9],
        [7, 3, 2]]

mat2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
```

El resultado devuelto será:
```python
[[4, 6, 7],
[0, 1, 3],
[0, -5, -7]]
```

---
---
### Tupla nombrada `Producto`

En los siguientes ejercicios se utilizará la siguiente `namedtuple`, que representa un producto de una tienda:

```python
Producto = namedtuple('Producto', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio'        # tipo float    
])
```

---

### Ejercicio 6 (1,25 puntos)

Implementa la función `calcula_factura`, que para una lista de **productos** calcula el desglose de la factura por categorías, incluyendo para cada categoría el precio total de los productos de esa categoría una vez aplicado el IVA correspondiente. El IVA que debe aplicarse a cada categoría viene indicado por un diccionario **iva_por_categoria**. Si una categoría no está contemplada en el diccionario recibido, se asume un IVA del 21%.

Por ejemplo, si se reciben los **productos**:
```python
[Producto(nombre="Camisa", categoria="Ropa", precio=20.0),
 Producto(nombre="Pantalón", categoria="Ropa", precio=30.0),
 Producto(nombre="Libro", categoria="Cultura", precio=15.0),
 Producto(nombre="Película", categoria="Cultura", precio=25.0),
 Producto(nombre="Comida", categoria="Alimentos", precio=10.0)]
 ```
 y el diccionario **iva_por_categoria** siguiente:
```python
{"Ropa": 0.10, "Cultura": 0.04}
```

El resultado devuelto será:
```python
{ "Ropa": 55.0,         # Calculado a partir de (20.0 * 1.10) + (30.0 * 1.10)
  "Cultura": 41.6,      # Calculado a partir de (15.0 * 1.04) + (25.0 * 1.04)
  "Alimentos": 12.1}    # Calculado a partir de (10.0 * 1.21)
```

---

### Ejercicio 7 (1,25 puntos)

Implementa la función `busca_producto_mas_caro`, que devuelve el producto más caro de una lista de **productos** y de una **categoria** dada. Si la **categoria** indicada es `None`, se busca el producto más caro de toda la lista de **productos**. 

---

### Ejercicio 8 (1,25 puntos)

Implementa la función `calcula_top_categorias`, que calcula el precio total de los **productos** de cada categoría, y devuelve las **n** categorías con el mayor precio total, junto con dichos totales. 

Por ejemplo, si los **productos** son:
```python
[Producto(nombre="Manzana", categoria="Fruta", precio=1.5), 
Producto(nombre="Pan", categoria="Panadería", precio=2.0), 
Producto(nombre="Pera", categoria="Fruta", precio=1.8), 
Producto(nombre="Croissant", categoria="Panadería", precio=3.5),
Producto(nombre="Leche", categoria="Lácteos", precio=2.2)]
```

y **n** es 2, el resultado será:
```python
[("Panadería", 5.5), ("Fruta", 3.3)]
```
    
