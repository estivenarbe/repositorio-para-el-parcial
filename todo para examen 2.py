club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

def estudiantes_en_al_menos_uno():
    """
    Retorna los estudiantes que están en AL MENOS UN club.
    (UNION de conjuntos)
    """

    """
    👉 SI EL PROFESOR ME PIDE "al menos uno":

    1. Se usa UNION (|)
    2. Porque queremos TODOS sin importar repeticiones
    """

    return club_ciencias | club_deportes | club_arte



def exactamente_dos_clubes():
    """
    Retorna estudiantes que están en EXACTAMENTE 2 clubes.
    """

    """
    👉 LOGICA CLAVE:

    1. Intersecciones de pares:
       - ciencias ∩ deportes
       - ciencias ∩ arte
       - deportes ∩ arte

    2. PERO quitar los que están en los 3
    """

    inter_cd = club_ciencias & club_deportes
    inter_ca = club_ciencias & club_arte
    inter_da = club_deportes & club_arte

    todos_los_tres = club_ciencias & club_deportes & club_arte

    resultado = (inter_cd | inter_ca | inter_da) - todos_los_tres

    return resultado



todos_estudiantes = {
    "Ana", "Carlos", "Diana", "Elena", "Felipe",
    "Gabriel", "Hugo", "Isabel", "Julia", "Karen",
    "Luis", "Marta"
}

def estudiantes_sin_club():
    """
    Retorna estudiantes que NO están en ningún club.
    """

    """
    👉 LOGICA:

    1. Primero saco TODOS los que están en algún club (UNION)
    2. Luego resto al total general
    """

    en_clubes = club_ciencias | club_deportes | club_arte

    return todos_estudiantes - en_clubes



def esta_en_mas_de_un_club(nombre):
    """
    Retorna True si el estudiante está en más de un club.
    """

    """
    👉 PASOS:

    1. Contar en cuántos conjuntos aparece
    2. Si es mayor a 1 → True
    """

    contador = 0

    if nombre in club_ciencias:
        contador += 1
    if nombre in club_deportes:
        contador += 1
    if nombre in club_arte:
        contador += 1

    return contador > 1



def club_con_mas_estudiantes():
    """
    Retorna el nombre del club con más estudiantes.
    """

    """
    👉 CLAVE:

    len(conjunto) → cantidad de elementos
    """

    tam_ciencias = len(club_ciencias)
    tam_deportes = len(club_deportes)
    tam_arte = len(club_arte)

    if tam_ciencias > tam_deportes and tam_ciencias > tam_arte:
        return "Ciencias"
    elif tam_deportes > tam_arte:
        return "Deportes"
    else:
        return "Arte"
    


def agregar_estudiante(club, nombre):
    """
    Agrega un estudiante a un club.
    """

    """
    👉 SI EL PROFESOR ME PIDE CONJUNTO:

    1. Verificar si ya existe
    2. Si NO → insertar
    """

    if nombre not in club:
        club.add(nombre)




def eliminar_de_todos(nombre):
    """
    Elimina un estudiante de todos los clubes.
    """

    """
    👉 CLAVE:

    discard → elimina sin error si no existe
    """

    club_ciencias.discard(nombre)
    club_deportes.discard(nombre)
    club_arte.discard(nombre)




class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class Conjunto:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        """
        👉 SI EL PROFESOR PIDE CON LISTA ENLAZADA:

        1. Recorrer lista
        2. Verificar si existe
        3. Si NO → insertar al inicio
        """

        actual = self.cabeza

        while actual:
            if actual.valor == valor:
                return  # Ya existe
            actual = actual.sig

        nuevo = Nodo(valor)
        nuevo.sig = self.cabeza
        self.cabeza = nuevo

    def pertenece(self, valor):
        actual = self.cabeza

        while actual:
            if actual.valor == valor:
                return True
            actual = actual.sig

        return False
    



"""
EJERCICIO 1:

Una empresa tiene usuarios registrados en tres plataformas:
Web, Móvil y Escritorio.

Resolver:

1. Obtener los usuarios que están en las TRES plataformas
2. Obtener los usuarios que están en EXACTAMENTE una plataforma
3. Obtener los usuarios que están en AL MENOS una plataforma
"""

web = {"Juan", "Ana", "Luis", "Carlos"}
movil = {"Ana", "Carlos", "Pedro", "Sofia"}
escritorio = {"Juan", "Carlos", "Elena", "Sofia"}


def usan_todas():
    """
    👉 INTERSECCION TOTAL
    Elementos comunes en los 3 conjuntos
    """
    return web & movil & escritorio


def usan_solo_una():
    """
    👉 LOGICA:

    1. Tomar cada conjunto
    2. Restar los otros dos
    3. Unir resultados
    """

    solo_web = web - movil - escritorio
    solo_movil = movil - web - escritorio
    solo_escritorio = escritorio - web - movil

    return solo_web | solo_movil | solo_escritorio


def usan_al_menos_una():
    """
    👉 UNION

    Todos los elementos sin importar repetición
    """
    return web | movil | escritorio






"""
EJERCICIO 2:

Un grupo de estudiantes está inscrito en tres cursos:
Matemáticas, Física y Programación.

Resolver:

1. Estudiantes en Matemáticas y Programación pero NO en Física
2. Estudiantes que están en EXACTAMENTE dos cursos
3. Estudiantes que NO están en ningún curso (usar conjunto total)
"""

matematicas = {"Ana", "Luis", "Carlos", "Marta"}
fisica = {"Luis", "Pedro", "Marta", "Elena"}
programacion = {"Ana", "Carlos", "Elena", "Sofia"}

todos = {"Ana", "Luis", "Carlos", "Marta", "Pedro", "Elena", "Sofia", "Raul"}


def mate_y_prog_sin_fisica():
    """
    👉 INTERSECCION - DIFERENCIA
    """
    return (matematicas & programacion) - fisica


def exactamente_dos():
    """
    👉 PASOS:

    1. Intersecciones de pares
    2. Quitar los que están en los 3
    """

    mf = matematicas & fisica
    mp = matematicas & programacion
    fp = fisica & programacion

    mfp = matematicas & fisica & programacion

    return (mf | mp | fp) - mfp


def sin_curso():
    """
    👉 DIFERENCIA

    Total - los que están en algún curso
    """
    en_cursos = matematicas | fisica | programacion
    return todos - en_cursos




"""
EJERCICIO 3:

Tres tiendas venden productos.

Resolver:

1. Productos que están en las TRES tiendas
2. Productos que están en EXACTAMENTE dos tiendas
3. Productos que están solo en una tienda
"""

tienda1 = {"Arroz", "Leche", "Pan", "Huevos"}
tienda2 = {"Leche", "Pan", "Queso", "Jugo"}
tienda3 = {"Pan", "Huevos", "Carne", "Jugo"}


def en_tres_tiendas():
    """
    👉 INTERSECCION TOTAL
    """
    return tienda1 & tienda2 & tienda3


def en_dos_tiendas():
    """
    👉 MISMA LOGICA CLASICA DE EXAMEN
    """

    t12 = tienda1 & tienda2
    t13 = tienda1 & tienda3
    t23 = tienda2 & tienda3

    t123 = tienda1 & tienda2 & tienda3

    return (t12 | t13 | t23) - t123


def solo_una_tienda():
    """
    👉 DIFERENCIAS INDIVIDUALES
    """

    solo1 = tienda1 - tienda2 - tienda3
    solo2 = tienda2 - tienda1 - tienda3
    solo3 = tienda3 - tienda1 - tienda2

    return solo1 | solo2 | solo3





"""
EJERCICIO 4:

Un sistema tiene:
- Usuarios registrados
- Usuarios logueados
- Usuarios premium

Resolver:

1. Usuarios logueados que NO están registrados (error)
2. Usuarios premium que están logueados
3. Usuarios registrados que NO han iniciado sesión
"""

registrados = {"Ana", "Luis", "Carlos", "Marta"}
logueados = {"Carlos", "Luis", "Pedro"}
premium = {"Luis", "Marta", "Pedro"}


def logueados_invalidos():
    """
    👉 DIFERENCIA
    """
    return logueados - registrados


def premium_logueados():
    """
    👉 INTERSECCION
    """
    return premium & logueados


def registrados_no_logueados():
    """
    👉 DIFERENCIA
    """
    return registrados - logueados




"""
EJERCICIO 5:

Un grupo de personas practica:
Fútbol, Baloncesto y Natación.

Resolver:

1. Personas que practican al menos un deporte
2. Personas que practican exactamente dos deportes
3. Personas que solo practican fútbol
"""

futbol = {"Juan", "Pedro", "Luis", "Carlos"}
baloncesto = {"Luis", "Carlos", "Ana", "Sofia"}
natacion = {"Pedro", "Ana", "Carlos", "Elena"}


def al_menos_uno():
    """
    👉 UNION
    """
    return futbol | baloncesto | natacion


def exactamente_dos_deportes():
    """
    👉 MISMA LOGICA CLAVE
    """

    fb = futbol & baloncesto
    fn = futbol & natacion
    bn = baloncesto & natacion

    fbn = futbol & baloncesto & natacion

    return (fb | fn | bn) - fbn


def solo_futbol():
    """
    👉 DIFERENCIA
    """
    return futbol - baloncesto - natacion





"""
🔥 SIEMPRE PIENSA ASÍ:

INTERSECCION → &
UNION → |
DIFERENCIA → -
DIF SIMETRICA → ^

👉 EXACTAMENTE 1:
A - B - C  (para cada uno)

👉 EXACTAMENTE 2:
(intersecciones de pares) - (intersección de los 3)

👉 AL MENOS UNO:
UNION

👉 NINGUNO:
TOTAL - UNION
"""





"""
ESTRUCTURA BASE: CONJUNTO CON LISTA ENLAZADA

👉 ESTO SIEMPRE TE LO PUEDEN PEDIR EN EL EXAMEN
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
        👉 INSERTAR SIN DUPLICADOS

        1. Recorrer lista
        2. Si existe → NO insertar
        3. Si no → insertar al inicio
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
        👉 BUSCAR ELEMENTO
        """

        actual = self.cabeza

        while actual:
            if actual.valor == valor:
                return True
            actual = actual.sig

        return False

    def mostrar(self):
        """
        👉 SOLO PARA VER RESULTADOS
        """

        elementos = []
        actual = self.cabeza

        while actual:
            elementos.append(actual.valor)
            actual = actual.sig

        return elementos
    




"""
EJERCICIO 1:

Dado dos conjuntos A y B (implementados con listas enlazadas):

Resolver:

1. UNION (A ∪ B)
2. INTERSECCION (A ∩ B)
3. DIFERENCIA (A - B)
"""

def union(A, B):
    """
    👉 LOGICA:

    1. Copiar todos los de A
    2. Insertar los de B (sin duplicar)
    """

    resultado = Conjunto()

    actual = A.cabeza
    while actual:
        resultado.insertar(actual.valor)
        actual = actual.sig

    actual = B.cabeza
    while actual:
        resultado.insertar(actual.valor)
        actual = actual.sig

    return resultado


def interseccion(A, B):
    """
    👉 SOLO ELEMENTOS COMUNES
    """

    resultado = Conjunto()

    actual = A.cabeza
    while actual:
        if B.pertenece(actual.valor):
            resultado.insertar(actual.valor)
        actual = actual.sig

    return resultado


def diferencia(A, B):
    """
    👉 ELEMENTOS EN A QUE NO ESTÁN EN B
    """

    resultado = Conjunto()

    actual = A.cabeza
    while actual:
        if not B.pertenece(actual.valor):
            resultado.insertar(actual.valor)
        actual = actual.sig

    return resultado





"""
EJERCICIO 2:

Dados tres conjuntos A, B y C:

Resolver:

1. Elementos en los TRES conjuntos
2. Elementos en EXACTAMENTE DOS conjuntos
3. Elementos en EXACTAMENTE UNO
"""

def interseccion_tres(A, B, C):
    """
    👉 A ∩ B ∩ C
    """

    resultado = Conjunto()

    actual = A.cabeza
    while actual:
        if B.pertenece(actual.valor) and C.pertenece(actual.valor):
            resultado.insertar(actual.valor)
        actual = actual.sig

    return resultado


def exactamente_dos(A, B, C):
    """
    👉 LOGICA CLAVE:

    (AB ∪ AC ∪ BC) - (ABC)
    """

    AB = interseccion(A, B)
    AC = interseccion(A, C)
    BC = interseccion(B, C)

    ABC = interseccion_tres(A, B, C)

    temp = union(union(AB, AC), BC)

    return diferencia(temp, ABC)


def exactamente_uno(A, B, C):
    """
    👉 SOLO EN UNO

    A - B - C  (y repetir para cada uno)
    """

    soloA = diferencia(diferencia(A, B), C)
    soloB = diferencia(diferencia(B, A), C)
    soloC = diferencia(diferencia(C, A), B)

    return union(union(soloA, soloB), soloC)





"""
EJERCICIO 3:

Dados dos conjuntos A y B:

Resolver:

1. Verificar si A es subconjunto de B
2. Verificar si son iguales
3. Verificar si son disjuntos
"""

def es_subconjunto(A, B):
    """
    👉 TODOS los elementos de A deben estar en B
    """

    actual = A.cabeza

    while actual:
        if not B.pertenece(actual.valor):
            return False
        actual = actual.sig

    return True


def son_iguales(A, B):
    """
    👉 A ⊆ B y B ⊆ A
    """

    return es_subconjunto(A, B) and es_subconjunto(B, A)


def son_disjuntos(A, B):
    """
    👉 NO tienen elementos en común
    """

    actual = A.cabeza

    while actual:
        if B.pertenece(actual.valor):
            return False
        actual = actual.sig

    return True




"""
EJERCICIO 4:

Tres conjuntos representan usuarios:

A: registrados
B: logueados
C: premium

Resolver:

1. Usuarios logueados pero NO registrados
2. Usuarios premium y logueados
3. Usuarios registrados que NO son premium
"""

def logueados_no_registrados(A, B):
    return diferencia(B, A)


def premium_logueados(B, C):
    return interseccion(B, C)


def registrados_no_premium(A, C):
    return diferencia(A, C)






"""
EJERCICIO 5:

Implementar:

1. Contar elementos de un conjunto
2. Determinar si está vacío
3. Obtener el elemento mayor (asumiendo números)
"""

def contar(conj):
    """
    👉 RECORRER Y CONTAR
    """

    contador = 0
    actual = conj.cabeza

    while actual:
        contador += 1
        actual = actual.sig

    return contador


def esta_vacio(conj):
    """
    👉 SI cabeza es None
    """
    return conj.cabeza is None


def mayor(conj):
    """
    👉 BUSCAR EL MAYOR
    """

    actual = conj.cabeza
    if actual is None:
        return None

    maximo = actual.valor

    while actual:
        if actual.valor > maximo:
            maximo = actual.valor
        actual = actual.sig

    return maximo






"""
🔥 SI EL PROFESOR DICE:

👉 UNION:
recorrer A + insertar B

👉 INTERSECCION:
si pertenece en ambos

👉 DIFERENCIA:
si NO pertenece en el otro

👉 SUBCONJUNTO:
todos los de A deben estar en B

👉 EXACTAMENTE 2:
(AB ∪ AC ∪ BC) - (ABC)

👉 EXACTAMENTE 1:
(A - B - C) ∪ ...
"""







"""
💀 PARCIAL FINAL – ALGORITMOS 4

TEMA: Conjuntos implementados con listas enlazadas

INSTRUCCIONES:
- NO usar estructuras de Python como set()
- TODO debe hacerse con listas enlazadas
- Evitar duplicados
- Justificar lógica (aquí ya te dejo guía tipo examen)

--------------------------------------------------
PUNTO 0 (BASE OBLIGATORIA)

Implementar la estructura de conjunto con lista enlazada
con las operaciones:

1. insertar (sin duplicados)
2. pertenece
3. eliminar
4. mostrar
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
        👉 TRAMPA CLÁSICA: NO permitir duplicados
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
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.sig
        return False

    def eliminar(self, valor):
        """
        👉 TRAMPA:

        1. Eliminar cabeza
        2. Eliminar en medio
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
PUNTO 1:

Dados dos conjuntos A y B:

1. UNION
2. INTERSECCION
3. DIFERENCIA (A - B)

👉 TRAMPA: No repetir elementos
"""
# --------------------------------------------------

def union(A, B):
    resultado = Conjunto()

    actual = A.cabeza
    while actual:
        resultado.insertar(actual.valor)
        actual = actual.sig

    actual = B.cabeza
    while actual:
        resultado.insertar(actual.valor)
        actual = actual.sig

    return resultado


def interseccion(A, B):
    resultado = Conjunto()

    actual = A.cabeza
    while actual:
        if B.pertenece(actual.valor):
            resultado.insertar(actual.valor)
        actual = actual.sig

    return resultado


def diferencia(A, B):
    resultado = Conjunto()

    actual = A.cabeza
    while actual:
        if not B.pertenece(actual.valor):
            resultado.insertar(actual.valor)
        actual = actual.sig

    return resultado


# --------------------------------------------------
"""
PUNTO 2:

Dados tres conjuntos A, B y C:

1. Elementos en los TRES conjuntos
2. Elementos en EXACTAMENTE DOS conjuntos
3. Elementos en EXACTAMENTE UNO

👉 TRAMPA FUERTE:
No confundir EXACTAMENTE con "al menos"
"""
# --------------------------------------------------

def interseccion_tres(A, B, C):
    resultado = Conjunto()

    actual = A.cabeza
    while actual:
        if B.pertenece(actual.valor) and C.pertenece(actual.valor):
            resultado.insertar(actual.valor)
        actual = actual.sig

    return resultado


def exactamente_dos(A, B, C):
    """
    👉 FORMULA CLAVE:

    (AB ∪ AC ∪ BC) - (ABC)
    """

    AB = interseccion(A, B)
    AC = interseccion(A, C)
    BC = interseccion(B, C)

    ABC = interseccion_tres(A, B, C)

    temp = union(union(AB, AC), BC)

    return diferencia(temp, ABC)


def exactamente_uno(A, B, C):
    """
    👉 TRAMPA:

    NO es unión directa
    """

    soloA = diferencia(diferencia(A, B), C)
    soloB = diferencia(diferencia(B, A), C)
    soloC = diferencia(diferencia(C, A), B)

    return union(union(soloA, soloB), soloC)

