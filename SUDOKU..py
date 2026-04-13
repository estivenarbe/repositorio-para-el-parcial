# ================================
# CONSTANTE PARA SUDOKU
# ================================

"""
👉 AQUÍ DEFINIMOS LOS NÚMEROS VÁLIDOS DEL SUDOKU

1. Un Sudoku válido tiene números del 1 al 9
2. Usamos un conjunto (set) porque:
   - No permite repetidos
   - Es fácil comparar

"""
NUMEROS_VALIDOS = set(range(1, 10))


# ================================
# PARTE 1: SUDOKU
# ================================

# ✔️ Validar una fila
def validar_fila(tablero, num_fila):

    """
    👉 SI EL PROFESOR ME PIDE VALIDAR UNA FILA:

    1. Tomo la fila del tablero
    2. La convierto en conjunto
    3. Comparo con los números válidos

    ✔ Si son iguales → la fila es correcta
    """

    # Obtenemos la fila completa
    fila = tablero[num_fila]
   
    # Convertimos a conjunto y comparamos
    return set(fila) == NUMEROS_VALIDOS


# ✔️ Validar una columna
def validar_columna(tablero, num_columna):

    """
    👉 SI EL PROFESOR ME PIDE VALIDAR UNA COLUMNA:

    1. Recorro todas las filas
    2. Extraigo el valor de la columna
    3. Formo una lista
    4. La convierto en conjunto
    5. Comparo con los números válidos

    ✔ Si son iguales → la columna es correcta
    """

    # Extraemos la columna recorriendo todas las filas
    columna = [tablero[i][num_columna] for i in range(9)]
   
    # Comparamos como conjunto
    return set(columna) == NUMEROS_VALIDOS


# ✔️ Validar subcuadro 3x3
def validar_subcuadro(tablero, fila_inicio, col_inicio):

    """
    👉 SI EL PROFESOR ME PIDE VALIDAR UN SUBCUADRO:

    1. Recorro un bloque de 3x3
    2. Guardo todos los elementos
    3. Los convierto en conjunto
    4. Comparo con los números válidos

    ✔ Si son iguales → el subcuadro es correcto
    """

    elementos = []
   
    # Recorremos bloque 3x3
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(col_inicio, col_inicio + 3):
            elementos.append(tablero[i][j])
   
    # Validamos con conjunto
    return set(elementos) == NUMEROS_VALIDOS


# ================================
# PARTE 2: LISTAS ENLAZADAS
# ================================

"""
👉 AQUÍ IMPLEMENTAMOS CONJUNTOS CON LISTAS ENLAZADAS

1. No usamos listas normales
2. Usamos nodos enlazados
3. Simulamos un conjunto (sin repetidos)
"""

# Nodo de lista enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Clase conjunto usando lista enlazada
class Conjunto:
    def __init__(self):
        self.cabeza = None

    # Agregar elemento (sin duplicados)
    def agregar(self, dato):

        """
        👉 SI EL PROFESOR ME PIDE AGREGAR A UN CONJUNTO:

        1. Verifico si ya existe
        2. Si NO existe → lo agrego
        3. Se inserta al inicio (lista enlazada)

        ✔ Evitamos duplicados
        """

        if not self.pertenece(dato):
            nuevo = Nodo(dato)
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

    # Verificar si un elemento pertenece
    def pertenece(self, dato):

        """
        👉 SI EL PROFESOR ME PIDE BUSCAR UN ELEMENTO:

        1. Recorro la lista nodo por nodo
        2. Comparo cada dato
        3. Si lo encuentro → True
        4. Si no → False
        """

        actual = self.cabeza
       
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
       
        return False


# ✔️ Verificar si A es subconjunto de B
def es_subconjunto(conjunto_a, conjunto_b):

    """
    👉 SI EL PROFESOR ME PIDE SUBCONJUNTO:

    1. Recorro todos los elementos de A
    2. Verifico si están en B
    3. Si alguno NO está → False
    4. Si todos están → True

    ✔ A ⊆ B
    """

    actual = conjunto_a.cabeza
   
    while actual:
        if not conjunto_b.pertenece(actual.dato):
            return False
       
        actual = actual.siguiente
   
    return True


# ✔️ Verificar permisos
def tiene_permisos(permisos_usuario, permisos_requeridos):

    """
    👉 SI EL PROFESOR ME PIDE VALIDAR PERMISOS:

    1. Verifico si los permisos requeridos
       están dentro de los del usuario

    2. Esto es:
       requeridos ⊆ usuario

    ✔ Si cumple → tiene permisos
    """

    return es_subconjunto(permisos_requeridos, permisos_usuario)


# ================================
# EXTRA: UNION DE CONJUNTOS
# ================================

def union(conjunto_a, conjunto_b):

    """
    👉 SI EL PROFESOR ME PIDE "AL MENOS UNO":

    1. Se usa UNION (∪)
    2. Porque queremos TODOS los elementos
       sin importar repeticiones

    3. Resultado:
       Elementos de A + Elementos de B
       sin duplicados
    """

    resultado = Conjunto()

    # Agregar elementos de A
    actual = conjunto_a.cabeza
    while actual:
        resultado.agregar(actual.dato)
        actual = actual.siguiente

    # Agregar elementos de B
    actual = conjunto_b.cabeza
    while actual:
        resultado.agregar(actual.dato)
        actual = actual.siguiente

    return resultado


# ================================
# EJEMPLO DE USO
# ================================

"""
👉 EJEMPLO CLAVE PARA EXAMEN:

"Retorna los estudiantes que están en AL MENOS UN club"

✔ Esto significa:
   UNION de conjuntos
"""

club1 = Conjunto()
club1.agregar("Ana")
club1.agregar("Luis")

club2 = Conjunto()
club2.agregar("Luis")
club2.agregar("Carlos")

resultado = union(club1, club2)

print("Estudiantes en al menos un club:")
actual = resultado.cabeza
while actual:
    print(actual.dato)
    actual = actual.siguiente



"""
💀 PARCIAL FINAL – ALGORITMOS 4

TEMA: Conjuntos implementados con listas enlazadas

INSTRUCCIONES:
- NO usar estructuras de Python como set()
- TODO con listas enlazadas
- Evitar duplicados
- Explicar con:

👉 SI EL PROFESOR ME PIDE...

--------------------------------------------------
PUNTO 0 (BASE)
--------------------------------------------------
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class Conjunto:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):

        """
        👉 SI EL PROFESOR ME PIDE INSERTAR:

        1. No permitir duplicados
        2. Recorrer antes de insertar
        """

        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return
            actual = actual.sig

        nuevo = Nodo(valor)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def pertenece(self, valor):

        """
        👉 SI EL PROFESOR ME PIDE BUSCAR:

        1. Recorrer nodo por nodo
        """

        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.sig
        return False

    def eliminar(self, valor):

        """
        👉 SI EL PROFESOR ME PIDE ELIMINAR:

        1. Caso cabeza
        2. Caso medio
        """

        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior is None:
                    self.cabeza = actual.sig
                else:
                    anterior.sig = actual.sig
                return
            anterior = actual
            actual = actual.sig

    def mostrar(self):
        elementos = []
        actual = self.cabeza

        while actual:
            elementos.append(actual.valor)
            actual = actual.sig

        return elementos


# --------------------------------------------------
"""
PUNTO 1: OPERACIONES BÁSICAS
--------------------------------------------------
"""

def union(A, B):

    """
    Retorna elementos en AL MENOS UNO

    👉 SI EL PROFESOR ME PIDE "al menos uno":

    1. UNION
    2. Todos sin repetir
    """

    R = Conjunto()

    actual = A.cabeza
    while actual:
        R.insertar(actual.valor)
        actual = actual.sig

    actual = B.cabeza
    while actual:
        R.insertar(actual.valor)
        actual = actual.sig

    return R


def interseccion(A, B):

    """
    Retorna elementos en AMBOS

    👉 SI EL PROFESOR ME PIDE "ambos":

    1. INTERSECCIÓN
    """

    R = Conjunto()

    actual = A.cabeza
    while actual:
        if B.pertenece(actual.valor):
            R.insertar(actual.valor)
        actual = actual.sig

    return R


def diferencia(A, B):

    """
    Retorna elementos SOLO EN A

    👉 SI EL PROFESOR ME PIDE "solo en A":

    1. DIFERENCIA
    """

    R = Conjunto()

    actual = A.cabeza
    while actual:
        if not B.pertenece(actual.valor):
            R.insertar(actual.valor)
        actual = actual.sig

    return R


def subconjunto(A, B):

    """
    Verifica A ⊆ B

    👉 SI EL PROFESOR ME PIDE "contenido":

    1. Todos los de A deben estar en B
    """

    actual = A.cabeza
    while actual:
        if not B.pertenece(actual.valor):
            return False
        actual = actual.sig
    return True


# --------------------------------------------------
"""
PUNTO 2: CLUBES (EJEMPLO CLÁSICO)
--------------------------------------------------
"""

clubA = Conjunto()
clubA.insertar("Ana")
clubA.insertar("Luis")

clubB = Conjunto()
clubB.insertar("Luis")
clubB.insertar("Carlos")

# Al menos uno
print("Clubes UNION:", union(clubA, clubB).mostrar())

# Ambos
print("Clubes INTERSECCIÓN:", interseccion(clubA, clubB).mostrar())

# Solo en A
print("Clubes DIFERENCIA:", diferencia(clubA, clubB).mostrar())


# --------------------------------------------------
"""
PUNTO 3: CURSOS
--------------------------------------------------
"""

curso1 = Conjunto()
curso1.insertar("Juan")
curso1.insertar("Maria")

curso2 = Conjunto()
curso2.insertar("Maria")
curso2.insertar("Pedro")

print("Cursos en ambos:", interseccion(curso1, curso2).mostrar())

print("¿curso1 ⊆ curso2?:", subconjunto(curso1, curso2))


# --------------------------------------------------
"""
PUNTO 4: PERMISOS
--------------------------------------------------
"""

usuario = Conjunto()
usuario.insertar("leer")
usuario.insertar("escribir")

requeridos = Conjunto()
requeridos.insertar("leer")

"""
👉 SI EL PROFESOR ME PIDE "tiene permisos":

1. requeridos ⊆ usuario
"""

print("Tiene permisos:", subconjunto(requeridos, usuario))

"""
👉 SI EL PROFESOR ME PIDE "faltan permisos":

1. DIFERENCIA
2. requeridos - usuario
"""

print("Permisos faltantes:", diferencia(requeridos, usuario).mostrar())


# --------------------------------------------------
"""
PUNTO 5: INVENTARIO
--------------------------------------------------
"""

bodegaA = Conjunto()
bodegaA.insertar("Laptop")
bodegaA.insertar("Mouse")

bodegaB = Conjunto()
bodegaB.insertar("Mouse")
bodegaB.insertar("Teclado")

print("Productos en ambas:", interseccion(bodegaA, bodegaB).mostrar())
print("Productos en alguna:", union(bodegaA, bodegaB).mostrar())


# --------------------------------------------------
"""
PUNTO 6: REDES SOCIALES
--------------------------------------------------
"""

amigos1 = Conjunto()
amigos1.insertar("Pedro")
amigos1.insertar("Juan")

amigos2 = Conjunto()
amigos2.insertar("Juan")
amigos2.insertar("Luis")

print("Amigos en común:", interseccion(amigos1, amigos2).mostrar())
print("Todos los amigos:", union(amigos1, amigos2).mostrar())


# --------------------------------------------------
"""
PUNTO 7: TRAMPA – IGUALDAD
--------------------------------------------------
"""

"""
👉 SI EL PROFESOR ME PIDE "iguales":

1. A ⊆ B
2. B ⊆ A
"""

def iguales(A, B):
    return subconjunto(A, B) and subconjunto(B, A)


print("¿Son iguales?:", iguales(clubA, clubB))


# --------------------------------------------------
"""
PUNTO 8: DIFERENCIA SIMÉTRICA
--------------------------------------------------
"""

"""
👉 SI EL PROFESOR ME PIDE:

"en uno pero no en ambos"

1. (A - B) ∪ (B - A)
"""

def diferencia_simetrica(A, B):
    return union(diferencia(A, B), diferencia(B, A))


print("Diferencia simétrica:", diferencia_simetrica(clubA, clubB).mostrar())
