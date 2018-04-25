class Vertice(object):
    def __init__(self, no):
        self.id = no
        self.adjacentes = {}

    def add_vizinho(self, vizinho, peso=0):
        self.adjacentes[vizinho] = peso

    def get_conexoes(self):
        return self.adjacentes.keys()

    def get_id(self):
        return self.id

    def get_custo(self, vizinho):
        return self.adjacentes[vizinho]

    def __str__(self):
        return str(self.id) + ' Adjacentes: ' + str([x.id for x in self.adjacentes])


class Grafo(object):
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertice(self, no):
        self.num_vertices = self.num_vertices + 1
        novoVertice = Vertice(no)
        self.vertices[no] = novoVertice
        return novoVertice

    def get_vertice(self, no):
        if no in self.vertices:
            return self.vertices[no]
        else:
            return None

    def add_aresta(self, de, para, custo=0):
        if de not in self.vertices:
            self.add_vertice(de)
        if para not in self.vertices:
            self.add_vertice(para)

        self.vertices[de].add_vizinho(self.vertices[de], custo)
        self.vertices[para].add_vizinho(self.vertices[para], custo)

    def get_vertices(self):
        return self.vertices.keys()
