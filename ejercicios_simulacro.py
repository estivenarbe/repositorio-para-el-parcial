"""
═══════════════════════════════════════════════════════════════════════
PARCIAL FINAL - ALGORITMOS Y ESTRUCTURAS

👉 SI EL PROFESOR ME PIDE:
- Validar datos → uso expresiones regulares
- Guardar datos dinámicos → uso lista enlazada
- Evitar repetidos → uso conjunto
- Optimizar recursividad → uso memorización
═══════════════════════════════════════════════════════════════════════
"""

import re

# ═══════════════════════════════════════════════════════════════════════
# PUNTO 1: EXPRESIONES REGULARES
# ═══════════════════════════════════════════════════════════════════════

def validar_email(email):
    """
    👉 SI EL PROFESOR ME PIDE VALIDAR UN EMAIL:

    1. Defino un patrón con regex
    2. Uso re.match para verificar
    3. Retorno True o False
    """

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # formato texto@texto.dominio
    return re.match(patron, email) is not None


def extraer_prioridad(texto):
    """
    👉 SI EL PROFESOR ME PIDE EXTRAER UN DATO DE UN TEXTO:

    1. Uso re.search
    2. Capturo el número con ()
    3. Uso group(1)
    """

    match = re.search(r'\[P(\d)\]', texto)
    return int(match.group(1)) if match else None


# ═══════════════════════════════════════════════════════════════════════
# PUNTO 2: LISTA ENLAZADA + RECURSIVIDAD
# ═══════════════════════════════════════════════════════════════════════

class Nodo:
    """
    👉 SI EL PROFESOR ME PIDE UNA LISTA ENLAZADA:

    Creo un nodo con:
    - dato
    - referencia al siguiente
    """

    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        self.siguiente = None


class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar(self, descripcion, prioridad):
        """
        👉 SI ME PIDEN INSERTAR ORDENADO Y RECURSIVO:

        1. Creo nodo
        2. Llamo función recursiva
        """

        nuevo = Nodo(descripcion, prioridad)
        self.cabeza = self._agregar_rec(self.cabeza, nuevo)

    def _agregar_rec(self, actual, nuevo):
        """
        👉 CASO BASE:
        - Lista vacía
        - Mayor prioridad
        """

        if actual is None or nuevo.prioridad > actual.prioridad:
            nuevo.siguiente = actual
            return nuevo

        actual.siguiente = self._agregar_rec(actual.siguiente, nuevo)
        return actual

    def contar_pendientes(self, prioridad):
        """
        👉 SI ME PIDEN CONTAR CON RECURSIVIDAD
        """
        return self._contar_rec(self.cabeza, prioridad)

    def _contar_rec(self, nodo, prioridad):
        """
        👉 CASO BASE:
        nodo == None
        """

        if nodo is None:
            return 0

        contar = 1 if (not nodo.completada and nodo.prioridad == prioridad) else 0

        return contar + self._contar_rec(nodo.siguiente, prioridad)

    def limpiar_completadas(self):
        """
        👉 SI ME PIDEN ELIMINAR NODOS RECURSIVO
        """
        self.cabeza = self._limpiar_rec(self.cabeza)

    def _limpiar_rec(self, nodo):
        if nodo is None:
            return None

        if nodo.completada:
            return self._limpiar_rec(nodo.siguiente)

        nodo.siguiente = self._limpiar_rec(nodo.siguiente)
        return nodo


# ═══════════════════════════════════════════════════════════════════════
# PUNTO 3: CONJUNTOS CON LISTA ENLAZADA
# ═══════════════════════════════════════════════════════════════════════

class NodoSet:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    """
    👉 SI EL PROFESOR ME PIDE IMPLEMENTAR UN CONJUNTO:

    - No se permiten repetidos
    - Uso lista enlazada
    """

    def __init__(self):
        self.cabeza = None

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        """
        👉 SOLO AGREGO SI NO EXISTE
        """
        if self.pertenece(x):
            return

        nuevo = NodoSet(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def es_subconjunto(self, otro):
        """
        👉 SI ME PIDEN SUBCONJUNTO RECURSIVO
        """
        return self._subconjunto_rec(self.cabeza, otro)

    def _subconjunto_rec(self, nodo, otro):
        if nodo is None:
            return True

        if not otro.pertenece(nodo.dato):
            return False

        return self._subconjunto_rec(nodo.siguiente, otro)


# ═══════════════════════════════════════════════════════════════════════
# PUNTO 4: MEMORIZACIÓN
# ═══════════════════════════════════════════════════════════════════════

def formas_escalera(n, memo=None):
    """
    👉 SI EL PROFESOR ME PIDE MEMORIZACIÓN:

    1. Uso diccionario (memo)
    2. Guardo resultados ya calculados
    """

    if memo is None:
        memo = {}

    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = formas_escalera(n-1, memo) + formas_escalera(n-2, memo)

    return memo[n]

"""
👉 MISMA LÓGICA DEL PARCIAL 1 PERO CON OTRO CONTEXTO

SI EL PROFESOR CAMBIA EL PROBLEMA:
YO MANTENGO:
- regex
- lista enlazada
- conjuntos
- memoización
"""

import re

# ═══════════════════════════════════════════════════════════════════════
# REGEX
# ═══════════════════════════════════════════════════════════════════════

def validar_username(username):
    """
    👉 VALIDAR STRING CON REGLAS
    """

    patron = r'^[a-zA-Z0-9]{4,10}$'
    return re.match(patron, username) is not None


def extraer_edad(texto):
    """
    👉 EXTRAER NÚMERO DE TEXTO
    """

    match = re.search(r'Edad:\s*(\d+)', texto)
    return int(match.group(1)) if match else None


# ═══════════════════════════════════════════════════════════════════════
# LISTA ENLAZADA
# ═══════════════════════════════════════════════════════════════════════

class NodoUsuario:
    def __init__(self, username, edad):
        self.username = username
        self.edad = edad
        self.activo = True
        self.siguiente = None


class ListaUsuarios:
    def __init__(self):
        self.cabeza = None

    def agregar(self, username, edad):
        """
        👉 INSERTAR ORDENADO RECURSIVO
        """
        nuevo = NodoUsuario(username, edad)
        self.cabeza = self._agregar_rec(self.cabeza, nuevo)

    def _agregar_rec(self, actual, nuevo):
        if actual is None or nuevo.edad > actual.edad:
            nuevo.siguiente = actual
            return nuevo

        actual.siguiente = self._agregar_rec(actual.siguiente, nuevo)
        return actual

    def contar_mayores(self, edad):
        """
        👉 CONTAR RECURSIVO
        """
        return self._contar_rec(self.cabeza, edad)

    def _contar_rec(self, nodo, edad):
        if nodo is None:
            return 0

        contar = 1 if (nodo.activo and nodo.edad >= edad) else 0

        return contar + self._contar_rec(nodo.siguiente, edad)

    def eliminar_inactivos(self):
        """
        👉 ELIMINAR NODOS RECURSIVO
        """
        self.cabeza = self._eliminar_rec(self.cabeza)

    def _eliminar_rec(self, nodo):
        if nodo is None:
            return None

        if not nodo.activo:
            return self._eliminar_rec(nodo.siguiente)

        nodo.siguiente = self._eliminar_rec(nodo.siguiente)
        return nodo


# ═══════════════════════════════════════════════════════════════════════
# CONJUNTOS
# ═══════════════════════════════════════════════════════════════════════

class NodoRol:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Roles:
    def __init__(self):
        self.cabeza = None

    def agregar(self, x):
        """
        👉 EVITAR REPETIDOS
        """
        if self.pertenece(x):
            return

        nuevo = NodoRol(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def es_subconjunto(self, otro):
        """
        👉 SUBCONJUNTO RECURSIVO
        """
        return self._rec(self.cabeza, otro)

    def _rec(self, nodo, otro):
        if nodo is None:
            return True

        if not otro.pertenece(nodo.dato):
            return False

        return self._rec(nodo.siguiente, otro)


# ═══════════════════════════════════════════════════════════════════════
# MEMORIZACIÓN
# ═══════════════════════════════════════════════════════════════════════

def interacciones(n, memo=None):
    """
    👉 MEMORIZACIÓN CON 3 OPCIONES (1,2,3)
    """

    if memo is None:
        memo = {}

    if n == 0:
        return 1
    if n < 0:
        return 0

    if n in memo:
        return memo[n]

    memo[n] = (
        interacciones(n-1, memo) +
        interacciones(n-2, memo) +
        interacciones(n-3, memo)
    )

    return memo[n]