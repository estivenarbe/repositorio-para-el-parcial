"""
═══════════════════════════════════════════════════════════════════════
PARCIAL 1 - ALGORITMOS Y PROGRAMACIÓN 4
SISTEMA: RED SOCIAL DE USUARIOS Y AMIGOS
═══════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Se desea implementar un sistema de red social.

Cada usuario:
Tiene un username (validado con regex)
Tiene una lista de amigos (SIN repetidos → c
onjunto)

SE PIDE:

1. Validar username con regex
2. Implementar lista enlazada de usuarios
3. Implementar conjunto de amigos (SIN set())
4. Funcionalidades:
   a) Agregar usuario
   b) Agregar amigo (sin duplicados)
   c) Amigos en común
   d) Sugerencias (diferencia)
   e) Verificar subconjunto
5. BONUS:
   - Eliminar usuario (RECURSIVO)
6. MEMORIZACIÓN:
   - Calcular conexiones posibles

RESTRICCIÓN:
❌ No usar set()
✔ Usar listas enlazadas
"""
import re

# ═══════════════════════════════════════════════════════════════════════
# REGEX
# ═══════════════════════════════════════════════════════════════════════

def validar_username(username):
    """
    👉 SI EL PROFESOR ME PIDE VALIDAR UN STRING:

    1. Defino patrón
    2. Uso re.match
    3. Retorno True/False
    """
    patron = r'^[a-zA-Z0-9]{4,10}$'
    return re.match(patron, username) is not None


# ═══════════════════════════════════════════════════════════════════════
# NODO PARA CONJUNTO
# ═══════════════════════════════════════════════════════════════════════

class NodoSet:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None


# ═══════════════════════════════════════════════════════════════════════
# CONJUNTO (AMIGOS)
# ═══════════════════════════════════════════════════════════════════════

class Conjunto:
    def __init__(self):
        self.cabeza = None

    def pertenece(self, x):
        """
        👉 PARA BUSCAR EN CONJUNTO:

        1. Recorrer lista
        2. Comparar
        """
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.sig
        return False

    def agregar(self, x):
        """
        👉 EVITAR DUPLICADOS:

        1. Verifico si existe
        2. Si no → inserto
        """
        if self.pertenece(x):
            return

        nuevo = NodoSet(x)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.dato)
            actual = actual.sig
        return lista

    def interseccion(self, otro):
        """
        👉 A ∩ B
        """
        res = Conjunto()
        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                res.agregar(actual.dato)
            actual = actual.sig
        return res

    def diferencia(self, otro):
        """
        👉 A - B
        """
        res = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                res.agregar(actual.dato)
            actual = actual.sig
        return res

    def es_subconjunto(self, otro):
        """
        👉 A ⊆ B
        """
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.sig
        return True


# ═══════════════════════════════════════════════════════════════════════
# LISTA ENLAZADA DE USUARIOS
# ═══════════════════════════════════════════════════════════════════════

class NodoUsuario:
    def __init__(self, username):
        self.username = username
        self.amigos = Conjunto()
        self.sig = None


class ListaUsuarios:
    def __init__(self):
        self.cabeza = None

    def agregar(self, username):
        """
        👉 SI EL PROFESOR PIDE VALIDAR + INSERTAR:

        1. Validar username
        2. Insertar en lista
        """
        if not validar_username(username):
            raise ValueError("Username inválido")

        nuevo = NodoUsuario(username)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def buscar(self, username):
        actual = self.cabeza
        while actual:
            if actual.username == username:
                return actual
            actual = actual.sig
        return None

    def eliminar(self, username):
        """
        👉 ELIMINAR RECURSIVO 🔥
        """
        self.cabeza = self._eliminar_rec(self.cabeza, username)

    def _eliminar_rec(self, nodo, username):
        if nodo is None:
            return None

        if nodo.username == username:
            return nodo.sig

        nodo.sig = self._eliminar_rec(nodo.sig, username)
        return nodo


# ═══════════════════════════════════════════════════════════════════════
# MEMORIZACIÓN
# ═══════════════════════════════════════════════════════════════════════

def conexiones(n, memo=None):
    """
    👉 SI EL PROFESOR ME PIDE MEMORIZACIÓN:

    1. Uso diccionario
    2. Evito recalcular
    """
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = conexiones(n-1, memo) + conexiones(n-2, memo)
    return memo[n]


# ═══════════════════════════════════════════════════════════════════════
# PRUEBA
# ═══════════════════════════════════════════════════════════════════════

red = ListaUsuarios()

red.agregar("Juan1")
red.agregar("Ana2")
red.agregar("Luis3")

red.buscar("Juan1").amigos.agregar("Ana2")
red.buscar("Juan1").amigos.agregar("Luis3")

print("Amigos de Juan:", red.buscar("Juan1").amigos.mostrar())
print("Conexiones posibles:", conexiones(5))
"""
═══════════════════════════════════════════════════════════════════════
PARCIAL 2 - ALGORITMOS Y PROGRAMACIÓN 4
SISTEMA: PLATAFORMA DE CURSOS ONLINE
═══════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Cada curso tiene estudiantes (CONJUNTO).

SE PIDE:

1. Validar emails (regex)
2. Lista enlazada de cursos
3. Conjuntos de estudiantes
4. Funciones:
   a) Unión
   b) Intersección
   c) Diferencia
   d) Subconjunto
5. BONUS:
   - Eliminar estudiante (RECURSIVO)
6. MEMORIZACIÓN:
   - Formas de completar cursos
"""

import re

# ═══════════════════════════════════════════════════════════════════════
# REGEX
# ═══════════════════════════════════════════════════════════════════════

def validar_email(email):
    """
    👉 VALIDAR EMAIL
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None


# ═══════════════════════════════════════════════════════════════════════
# NODO
# ═══════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None


# ═══════════════════════════════════════════════════════════════════════
# CONJUNTO
# ═══════════════════════════════════════════════════════════════════════

class Conjunto:
    def __init__(self):
        self.cabeza = None

    def contiene(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.sig
        return False

    def agregar(self, x):
        """
        👉 SIN DUPLICADOS
        """
        if self.contiene(x):
            return
        nuevo = Nodo(x)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def union(self, otro):
        """
        👉 A ∪ B
        """
        res = Conjunto()
        actual = self.cabeza
        while actual:
            res.agregar(actual.dato)
            actual = actual.sig

        actual = otro.cabeza
        while actual:
            res.agregar(actual.dato)
            actual = actual.sig

        return res

    def interseccion(self, otro):
        """
        👉 A ∩ B
        """
        res = Conjunto()
        actual = self.cabeza
        while actual:
            if otro.contiene(actual.dato):
                res.agregar(actual.dato)
            actual = actual.sig
        return res

    def diferencia(self, otro):
        """
        👉 A - B
        """
        res = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro.contiene(actual.dato):
                res.agregar(actual.dato)
            actual = actual.sig
        return res

    def es_subconjunto(self, otro):
        """
        👉 A ⊆ B
        """
        actual = self.cabeza
        while actual:
            if not otro.contiene(actual.dato):
                return False
            actual = actual.sig
        return True

    def eliminar(self, dato):
        """
        👉 ELIMINAR RECURSIVO 🔥
        """
        self.cabeza = self._eliminar_rec(self.cabeza, dato)

    def _eliminar_rec(self, nodo, dato):
        if nodo is None:
            return None

        if nodo.dato == dato:
            return nodo.sig

        nodo.sig = self._eliminar_rec(nodo.sig, dato)
        return nodo

    def mostrar(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.dato)
            actual = actual.sig
        return lista


# ═══════════════════════════════════════════════════════════════════════
# MEMORIZACIÓN
# ═══════════════════════════════════════════════════════════════════════

def formas(n, memo=None):
    """
    👉 MEMORIZACIÓN:

    1. Uso diccionario
    2. Guardo resultados
    """
    if memo is None:
        memo = {}

    if n == 0:
        return 1
    if n < 0:
        return 0

    if n in memo:
        return memo[n]

    memo[n] = formas(n-1, memo) + formas(n-2, memo)
    return memo[n]


# ═══════════════════════════════════════════════════════════════════════
# PRUEBA
# ═══════════════════════════════════════════════════════════════════════

curso1 = Conjunto()
curso2 = Conjunto()

for e in ["ana@mail.com", "luis@mail.com", "carlos@mail.com"]:
    if validar_email(e):
        curso1.agregar(e)

for e in ["luis@mail.com", "maria@mail.com"]:
    if validar_email(e):
        curso2.agregar(e)

print("Curso1:", curso1.mostrar())
print("Curso2:", curso2.mostrar())

print("Unión:", curso1.union(curso2).mostrar())
print("Intersección:", curso1.interseccion(curso2).mostrar())
print("Diferencia:", curso1.diferencia(curso2).mostrar())

print("Formas de completar cursos:", formas(5))
