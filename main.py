from vertice import Vertice
from graph_knn import Graph_knn, distancia_euclidiana
from matplotlib import pyplot as plt

def main():
    print('Grafo')

    # vertice_aux = Vertice(1, 2)
    # vertice_aux.adiciona_aresta(3)
    # vertice_aux.adiciona_aresta(5)
    # vertice_aux.adiciona_aresta(7)
    # print(vertice_aux.x, vertice_aux.y, vertice_aux.arestas, vertice_aux.qt_arestas)

    # grafo = []
    # grafo.append(Vertice(1, 1))
    # grafo[-1].adiciona_aresta(2)
    # grafo[-1].adiciona_aresta(3)
    # grafo.append(Vertice(2, 2))
    # grafo[-1].adiciona_aresta(3)
    # grafo.append(Vertice(3, 8))
    # grafo[-1].adiciona_aresta(0)
    # grafo[-1].adiciona_aresta(2)
    # grafo.append(Vertice(5, 3))
    # grafo[-1].adiciona_aresta(2)
    # for i in range(0, len(grafo)):
    #     print(f"Ponto {i}")
    #     grafo[i].exibe_vertice()

    grafo_knn = Graph_knn(10, 3)
    

if(__name__ == "__main__"):
    main()