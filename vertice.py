class Vertice():
    """Implementação de um vertice com coordenadas x e y."""

    def __init__(self, x, y):
        """Inicializa as estruturas base do vértice."""
        self.x = x
        self.y = y
        self.arestas = []

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coordenadas(self):
        return (self.x, self.y)

    def get_arestas(self):
        return self.arestas

    def adiciona_aresta(self, index, distancia=-1):
        for i in range(0, len(self.arestas)+1):
            if(i == len(self.arestas) or self.arestas[i][1] > distancia):
                self.arestas.insert(i, (index, distancia))
                break
        return self.arestas

    def exibe_vertice(self):
        print("Vértice ({}, {}) ligado aos pontos: {}".format(self.x, self.y, self.arestas))

    def __len__(self):
        return len(self.arestas)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)