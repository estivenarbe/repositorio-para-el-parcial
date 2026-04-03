"""
═══════════════════════════════════════════════════════════════════════
PARCIAL - CONJUNTOS CON LISTAS SIMPLEMENTE LIGADAS
SISTEMA: GESTIÓN DE CURSOS UNIVERSITARIOS
═══════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
La universidad desea analizar la inscripción de estudiantes en cursos.

Cada curso tiene un conjunto de estudiantes.
Se debe implementar un sistema usando LISTAS ENLAZADAS (sin usar set).

SE PIDE:

1. Implementar la estructura de conjunto
2. Insertar estudiantes (sin duplicados)
3. Implementar:
   - Unión
   - Intersección
   - Diferencia
   - Subconjunto
4. Funcionalidades:
   a) Estudiantes en común entre cursos
   b) Estudiantes exclusivos
   c) Total de estudiantes únicos
   d) Verificar si un curso está contenido en otro
   e) Estudiantes en TODOS los cursos
   f) Recomendación de cursos (basado en diferencia)
5. BONUS:
   - Eliminar estudiante (RECURSIVO)

RESTRICCIÓN:
❌ No usar set()
✔ Solo listas enlazadas
"""

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

    # 👉 BUSCAR ELEMENTO
    def contiene(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.sig
        return False

    # 👉 INSERTAR SIN DUPLICADOS
    def agregar(self, dato):
        if not self.contiene(dato):
            nuevo = Nodo(dato)
            nuevo.sig = self.cabeza
            self.cabeza = nuevo

    # 👉 MOSTRAR
    def mostrar(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.dato)
            actual = actual.sig
        return lista

    # 👉 TAMAÑO
    def tamaño(self):
        cont = 0
        actual = self.cabeza
        while actual:
            cont += 1
            actual = actual.sig
        return cont

    # 👉 UNIÓN
    def union(self, otro):
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

    # 👉 INTERSECCIÓN
    def interseccion(self, otro):
        res = Conjunto()
        actual = self.cabeza

        while actual:
            if otro.contiene(actual.dato):
                res.agregar(actual.dato)
            actual = actual.sig

        return res

    # 👉 DIFERENCIA
    def diferencia(self, otro):
        res = Conjunto()
        actual = self.cabeza

        while actual:
            if not otro.contiene(actual.dato):
                res.agregar(actual.dato)
            actual = actual.sig

        return res

    # 👉 SUBCONJUNTO
    def es_subconjunto(self, otro):
        actual = self.cabeza
        while actual:
            if not otro.contiene(actual.dato):
                return False
            actual = actual.sig
        return True

    # 👉 ELIMINAR RECURSIVO 🔥
    def eliminar(self, dato):
        self.cabeza = self._eliminar_rec(self.cabeza, dato)

    def _eliminar_rec(self, nodo, dato):
        if nodo is None:
            return None
        if nodo.dato == dato:
            return nodo.sig
        nodo.sig = self._eliminar_rec(nodo.sig, dato)
        return nodo


# ═══════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════

algoritmos = Conjunto()
bases_datos = Conjunto()
redes = Conjunto()

for est in ["Ana", "Carlos", "Diana", "Luis", "Pedro"]:
    algoritmos.agregar(est)

for est in ["Carlos", "Diana", "Maria", "Luis"]:
    bases_datos.agregar(est)

for est in ["Diana", "Pedro", "Luis", "Sofia"]:
    redes.agregar(est)


# ═══════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════

print("="*60)
print("UNIVERSIDAD - ANÁLISIS DE CURSOS")
print("="*60)

print("\nAlgoritmos:", algoritmos.mostrar())
print("Bases de Datos:", bases_datos.mostrar())
print("Redes:", redes.mostrar())


# 1. ESTUDIANTES EN COMÚN
print("\n1. EN COMÚN:")
print("Alg-BD:", algoritmos.interseccion(bases_datos).mostrar())
print("Alg-Redes:", algoritmos.interseccion(redes).mostrar())


# 2. EXCLUSIVOS
print("\n2. EXCLUSIVOS:")
print("Solo Algoritmos:", algoritmos.diferencia(bases_datos).diferencia(redes).mostrar())


# 3. TOTAL ESTUDIANTES
total = algoritmos.union(bases_datos).union(redes)
print("\n3. TOTAL:", total.mostrar())


# 4. SUBCONJUNTO
print("\n4. SUBCONJUNTO:")
print("¿BD ⊆ Algoritmos?:", bases_datos.es_subconjunto(algoritmos))


# 5. EN TODOS LOS CURSOS
todos = algoritmos.interseccion(bases_datos).interseccion(redes)
print("\n5. EN LOS 3:", todos.mostrar())


# 6. RECOMENDACIONES
print("\n6. RECOMENDACIONES:")
print("A estudiantes de Algoritmos sugerir BD:",
      bases_datos.diferencia(algoritmos).mostrar())


# 7. ELIMINAR (PRUEBA)
print("\n7. ELIMINAR:")
algoritmos.eliminar("Pedro")
print("Algoritmos sin Pedro:", algoritmos.mostrar())