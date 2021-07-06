from graph_knn import distancia_euclidiana

def busca_A(grafo, inicio, fim):
    print("BUSCA BEST FIRST")

    vertices = grafo.get_vertices()

    pilha = [inicio]
    visitados = [inicio]
    # antecessores = [-1]
    distancia_percorrida = 0
    distancia_caminho = -1
    caminho = []
    while pilha:
        vertice_antecessor = pilha[-1]
        print("Pilha:", pilha, "Distancia:", distancia_percorrida)

        

        for aresta in vertices[vertice_antecessor].get_arestas():
            if aresta[0] not in visitados:
                pilha.append(aresta[0])
                distancia_percorrida += aresta[1]
                if aresta[0] == fim:
                    print("Caminho: ", pilha, "Distancia:", distancia_percorrida)
                    if not caminho or distancia_percorrida < distancia_caminho or len(pilha) < len(caminho):
                        print("Novo caminho\n")
                        caminho = pilha.copy()
                        distancia_caminho = distancia_percorrida
                    distancia_percorrida -= aresta[1]
                    pilha.pop()
                    pilha.pop()
                else:
                    visitados.append(aresta[0])

                break

            if aresta == vertices[vertice_antecessor].arestas[-1]:
                distancia_percorrida -= aresta[1]
                pilha.pop()


    if not caminho:
        print(f"Não possui caminho de {inicio} até {fim}. :(")
    else:
        print("Tem caminho!")
        print(caminho)

    print()
    return caminho
        