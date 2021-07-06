import math
from vertice import Vertice
import random
from matplotlib import pyplot as plt
# from curses import *

def distancia_euclidiana(p1, p2):
    """Distância entre dois pontos com coordenadas [x, y]."""
    # if(len(p1) != 2 or len(p2) != 2): return False
    return math.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


def vetor_hash(base, x=0, y=0):
    """Hash para vértices em um plano 2d."""
    return x * pow(base, 1) + y * pow(base, 0)


def teste_insercao_nova_aresta(vertice, limite, index, distancia):
    """Testa se nova aresta deve ser criada, conectando dois pontos."""
    # Testa se ja atingiu o limite de arestas ou se a distancia do novo ponto é menor que a distancia do ponto mais distante
    if(len(vertice.arestas) < limite or vertice.arestas[-1][1] > distancia):
        # Insere nova aresta
        vertice.adiciona_aresta(index, distancia)

        # Remove vertice mais distante, caso tenha passado do limite de arestas
        if(len(vertice.arestas) > limite):
            vertice.arestas.pop()


class Graph_knn():
    """Implementação de um grafo knn."""
    def __init__(self, v, k):
        """Inicializa as estruturas base do grafo."""
        print(f"Criando grafo knn com {v} vertices, cada um deles com {k} arestas")
        print()

        self.v = v
        self.k = k

        # Inicializa o grafo vazio
        vertices = []
        hashs = []

        porcentagem = 0
        parte = v/100
        progresso = 0

        # Preenche o grafo com os v vértices com coordenadas aleatórias
        for i in range(0, v):
            while True:
                x = random.randint(0, v)
                y = random.randint(0, v)
                hash = vetor_hash(v+1, x, y)
                # print(f"ponto: ({x}, {y}) - hash: {hash}")
                if(hash not in hashs): break
                else: print("Gerou vértice já existente. Gera coordenadas novamente.")
            
            if(i >= progresso):
                print(f"Criação dos vértices {porcentagem:.0f}% concluído...")
                porcentagem = ((i+1)/v)*100
                progresso += parte
            
            hashs.append(hash)
            vertices.append(Vertice(x, y))

        print(f"Criação dos vértices {porcentagem:.0f}% concluído...")
        print()

        porcentagem = 0
        parte = v/100
        progresso = 0

        # Acha as distâncias entre todos os vértices
        for i in range(0, v):
            for j in range(i+1, v):
                distancia = distancia_euclidiana(vertices[i].get_coordenadas(), vertices[j].get_coordenadas())
                
                teste_insercao_nova_aresta(vertices[i], k, j, distancia)
                teste_insercao_nova_aresta(vertices[j], k, i, distancia)
            
            if(i >= progresso):
                print(f"Definição das arestas {porcentagem:.0f}% concluído...")
                porcentagem = ((i+1)/v)*100
                progresso += parte

        print(f"Definição das arestas {porcentagem:.0f}% concluído...")
        print()

        self.vertices = vertices
        self.exibe_grafo()
        print()
        print("Grafo criado!")
        print()

    
    def get_v(self):
        return self.v
    

    def get_k(self):
        return self.k


    def get_vertices(self):
        return self.vertices


    def exibe_grafo(self):
        for i in range(0, len(self.vertices)):
            print(f"{i} - ", end='')
            self.vertices[i].exibe_vertice()