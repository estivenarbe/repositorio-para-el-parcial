"""
═══════════════════════════════════════════════════════════════════════════════
                        QUIZ 2 - ESTRUCTURAS DE DATOS
                                  EXAMEN C
                    Sistema de Playlist de Música
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Spotify te ha contratado para implementar un sistema de playlist.
Debes usar listas enlazadas.

Cada canción tiene:
Nombre
Artista
Duración (segun
dos)

INSTRUCCIONES:
--------------
1. Usar listas enlazadas (NO listas de Python [])
2. Aplicar RECURSIVIDAD donde se indique
3. Validar datos de entrada
4. Manejar lista vacía correctamente
5. Tiempo: 90 minutos
"""


# ================== NODO ==================
class Cancion:
    def __init__(self, nombre, artista, duracion):
        """
        👉 SI EL PROFESOR ME PIDE CREAR UN NODO:

        1. Debo guardar los datos
        2. Crear el puntero siguiente
        3. Validar entradas
        """

        # VALIDACIONES
        if not nombre or not artista:
            raise ValueError("Nombre y artista no pueden estar vacíos")
        if duracion <= 0:
            raise ValueError("Duración debe ser mayor a 0")

        # ATRIBUTOS
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

        # PUNTERO (clave en listas enlazadas)
        self.siguiente = None


# ================== LISTA ==================
class Playlist:
    def __init__(self):
        """
        👉 SI EL PROFESOR ME PIDE UNA LISTA ENLAZADA:

        1. Solo necesito la cabeza
        2. Inicialmente es None
        """
        self.cabeza = None


    # ================== AGREGAR ==================
    def agregar(self, nombre, artista, duracion):
        """
        👉 SI EL PROFESOR ME PIDE INSERTAR AL FINAL:

        PASOS:
        1. Crear nodo
        2. Si está vacía → cabeza = nuevo
        3. Si no → recorrer
        4. Enlazar al final
        """

        nueva = Cancion(nombre, artista, duracion)

        # Lista vacía
        if self.cabeza is None:
            self.cabeza = nueva
            return

        # Recorrer
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        # Enlazar
        actual.siguiente = nueva


    # ================== MOSTRAR ==================
    def mostrar(self):
        """
        👉 SI EL PROFESOR ME PIDE RECORRER:

        1. Empiezo desde cabeza
        2. Avanzo con siguiente
        3. Paro cuando sea None
        """

        if self.cabeza is None:
            print("Lista vacía")
            return

        actual = self.cabeza
        while actual:
            print(f"🎵 {actual.nombre} - {actual.artista} ({actual.duracion}s)")
            actual = actual.siguiente


    # ================== RECURSIVO ==================
    def duracion_total(self):
        """
        👉 SI EL PROFESOR ME PIDE RECURSIVIDAD:

        1. Creo función auxiliar
        2. Paso la cabeza
        """
        return self._duracion_total_rec(self.cabeza)

    def _duracion_total_rec(self, nodo):
        """
        👉 PLANTILLA RECURSIVA:

        CASO BASE:
        - nodo es None → retorno 0

        CASO RECURSIVO:
        - sumo actual + llamada recursiva
        """

        if nodo is None:
            return 0

        return nodo.duracion + self._duracion_total_rec(nodo.siguiente)


    # ================== FILTRAR ==================
    def filtrar_artista(self, artista):
        """
        👉 SI EL PROFESOR ME PIDE DEVOLVER NUEVA LISTA:

        1. Crear nueva lista
        2. NO modificar original
        3. Usar recursividad
        """

        if not artista:
            raise ValueError("Artista vacío")

        nueva = Playlist()
        self._filtrar_rec(self.cabeza, artista.lower(), nueva)
        return nueva

    def _filtrar_rec(self, nodo, artista, nueva):
        """
        👉 RECORRIDO RECURSIVO CON CONDICIÓN:

        1. Caso base: nodo None
        2. Si cumple → agregar
        3. Llamar siguiente
        """

        if nodo is None:
            return

        if artista in nodo.artista.lower():
            nueva.agregar(nodo.nombre, nodo.artista, nodo.duracion)

        self._filtrar_rec(nodo.siguiente, artista, nueva)


    # ================== ELIMINAR ==================
    def eliminar_largas(self, max_duracion):
    

        if max_duracion <= 0:
            raise ValueError("Duración inválida")

        self.cabeza = self._eliminar_rec(self.cabeza, max_duracion)

    def _eliminar_rec(self, nodo, max_duracion):
        """
        👉 PLANTILLA CLAVE DE ELIMINACIÓN:

        1. Procesar siguiente
        2. Decidir si elimino o no
        """

        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_rec(nodo.siguiente, max_duracion)

        if nodo.duracion > max_duracion:
            return nodo.siguiente

        return nodo


# ================== PRUEBAS ==================
if __name__ == "__main__":
    p = Playlist()

    p.agregar("Song1", "Bad Bunny", 200)
    p.agregar("Song2", "Drake", 180)
    p.agregar("Song3", "Bad Bunny ft Drake", 400)
    p.agregar("Song4", "Karol G", 90)

    print("\n📋 Playlist:")
    p.mostrar()

    print("\n⏱️ Total:", p.duracion_total())

    print("\n🔍 Filtrar 'Bad Bunny':")
    f = p.filtrar_artista("Bad Bunny")
    f.mostrar()

    print("\n🗑️ Eliminar > 200s:")
    p.eliminar_largas(200)
    p.mostrar()
"""
═══════════════════════════════════════════════════════════════════════════════
                        QUIZ 2 - ESTRUCTURAS DE DATOS
                                  EXAMEN D
                    Sistema de Pedidos de Restaurante
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Un restaurante necesita gestionar pedidos en cola (FIFO).

Cada pedido tiene:
ID
nombre del cliente
total de la cuenta
estado (pendiente / entregado)

INSTRUCCIONES:
--------------
1. Usar listas enlazadas (NO listas de Python [])
2. Aplicar recursividad donde se indique
3. Validar datos de entrada
4. Manejar estructura vacía correctamente
5. Tiempo: 90 minutos
"""


# ================== NODO ==================
class Pedido:
    def __init__(self, id, cliente, total, estado="pendiente"):
        """
        👉 SI EL PROFESOR ME PIDE CREAR UN NODO:

        1. Guardar los datos
        2. Validar entradas
        3. Crear puntero siguiente
        """

        # VALIDACIONES
        if id < 0:
            raise ValueError("ID inválido")
        if not cliente:
            raise ValueError("Cliente vacío")
        if total <= 0:
            raise ValueError("Total inválido")
        if estado not in ["pendiente", "entregado"]:
            raise ValueError("Estado inválido")

        # ATRIBUTOS
        self.id = id
        self.cliente = cliente
        self.total = total
        self.estado = estado

        # PUNTERO
        self.siguiente = None


# ================== COLA ==================
class ColaPedidos:
    def __init__(self):
        """
        👉 SI EL PROFESOR ME PIDE UNA COLA:

        1. Necesito frente (inicio)
        2. Necesito final (último)
        3. Ambos empiezan en None
        """
        self.frente = None
        self.final = None


    # ================== VALIDAR ID ==================
    def _existe_id(self, id):
        """
        👉 SI EL PROFESOR ME PIDE VALIDAR DUPLICADOS:

        1. Recorrer la lista
        2. Comparar IDs
        """

        actual = self.frente
        while actual:
            if actual.id == id:
                return True
            actual = actual.siguiente

        return False


    # ================== ENCOLAR ==================
    def encolar(self, id, cliente, total):
        """
        👉 SI EL PROFESOR ME PIDE INSERTAR EN COLA (FIFO):

        PASOS:
        1. Validar duplicado
        2. Crear nodo
        3. Si está vacía → frente y final = nuevo
        4. Si no → insertar al final
        """

        if self._existe_id(id):
            raise ValueError("ID duplicado")

        nuevo = Pedido(id, cliente, total)

        # Cola vacía
        if self.frente is None:
            self.frente = self.final = nuevo
            return

        # Insertar al final
        self.final.siguiente = nuevo
        self.final = nuevo


    # ================== DESENCOLAR ==================
    def desencolar(self):
        """
        👉 SI EL PROFESOR ME PIDE ELIMINAR EN COLA:

        1. Se elimina el frente
        2. Se mueve el frente
        3. Si queda vacía → final = None
        """

        if self.frente is None:
            raise ValueError("Cola vacía")

        eliminado = self.frente
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        return eliminado


    # ================== MOSTRAR ==================
    def mostrar(self):
        """
        👉 SI EL PROFESOR ME PIDE RECORRER:

        Igual que lista enlazada
        """

        if self.frente is None:
            print("Cola vacía")
            return

        actual = self.frente
        while actual:
            print(f"🧾 ID:{actual.id} | {actual.cliente} | {actual.total} | {actual.estado}")
            actual = actual.siguiente


    # ================== TOTAL PENDIENTE ==================
    def total_pendiente(self):
        """
        👉 SI EL PROFESOR ME PIDE RECURSIVIDAD:

        1. Crear función auxiliar
        2. Trabajar desde frente
        """

        return self._total_rec(self.frente)

    def _total_rec(self, nodo):
        """
        👉 PLANTILLA RECURSIVA:

        CASO BASE:
        - nodo None → 0

        CASO RECURSIVO:
        - sumo solo si está pendiente
        """

        if nodo is None:
            return 0

        suma = nodo.total if nodo.estado == "pendiente" else 0

        return suma + self._total_rec(nodo.siguiente)


    # ================== BUSCAR CLIENTE ==================
    def buscar_cliente(self, nombre):
        """
        👉 SI EL PROFESOR ME PIDE NUEVA ESTRUCTURA:

        1. Validar entrada
        2. Crear nueva cola
        3. No modificar original
        """

        if not nombre:
            raise ValueError("Nombre vacío")

        nueva = ColaPedidos()
        self._buscar_rec(self.frente, nombre.lower(), nueva)
        return nueva

    def _buscar_rec(self, nodo, nombre, nueva):
        """
        👉 RECORRIDO RECURSIVO:

        1. Caso base
        2. Si cumple → agregar
        3. Llamar siguiente
        """

        if nodo is None:
            return

        if nombre in nodo.cliente.lower():
            nueva.encolar(nodo.id, nodo.cliente, nodo.total)

        self._buscar_rec(nodo.siguiente, nombre, nueva)


    # ================== ELIMINAR ENTREGADOS ==================
    def eliminar_entregados(self):
        """
        👉 SI EL PROFESOR ME PIDE ELIMINAR RECURSIVO:

        1. Reasignar frente
        2. Ajustar final
        """

        self.frente = self._eliminar_rec(self.frente)

        # Reajustar final (MUY IMPORTANTE EN COLAS)
        actual = self.frente
        self.final = None

        while actual:
            if actual.siguiente is None:
                self.final = actual
            actual = actual.siguiente

    def _eliminar_rec(self, nodo):
        """
        👉 PLANTILLA CLAVE:

        1. Procesar siguiente
        2. Decidir si eliminar
        """

        if nodo is None:
            return None

        nodo.siguiente = self._eliminar_rec(nodo.siguiente)

        if nodo.estado == "entregado":
            return nodo.siguiente

        return nodo


# ================== PRUEBAS ==================
if __name__ == "__main__":
    c = ColaPedidos()

    c.encolar(1, "Juan", 20000)
    c.encolar(2, "Maria", 30000)
    c.encolar(3, "Juan Perez", 15000)

    print("\n📋 Pedidos:")
    c.mostrar()

    print("\n⏱️ Total pendiente:", c.total_pendiente())

    print("\n🔍 Buscar 'Juan':")
    b = c.buscar_cliente("juan")
    b.mostrar()

    print("\n🗑️ Marcar y eliminar entregados:")
    c.frente.estado = "entregado"
    c.eliminar_entregados()
    c.mostrar()
