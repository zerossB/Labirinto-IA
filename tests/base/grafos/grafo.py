class Vertice:
    def __init__(self, node):
        self.id = node
        self.adjacente = {}

    def __str__(self):
        return str(self.id) + ' adjacente: ' + str([x.id for x in self.adjacente])

    def add_vizinho(self, vizinho, peso=0):
        self.adjacente[vizinho] = peso

    def get_connections(self):
        return self.adjacente.keys()

    def get_id(self):
        return self.id

    def get_peso(self, vizinho):
        return self.adjacente[vizinho]


class Grafo:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertice(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertice = Vertice(node)
        self.vertices[node] = new_vertice
        return new_vertice

    def get_vertice(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_aresta(self, frm, to, custo=0):
        if frm not in self.vertices:
            self.add_vertice(frm)
        if to not in self.vertices:
            self.add_vertice(to)

        self.vertices[frm].add_vizinho(self.vertices[to], custo)
        self.vertices[to].add_vizinho(self.vertices[frm], custo)

    def get_vertices(self):
        return self.vertices.keys()
