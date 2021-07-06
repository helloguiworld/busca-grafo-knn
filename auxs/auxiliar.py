def busca_best_first(grafo, inicio, fim):
    print("BUSCA BEST FIRST")

    vertices = grafo.get_vertices()

    fila = [inicio]
    visitados = [inicio]
    historico = [[inicio, -1]]
    antecessores = [-1]
    distancia = -1
    while fila:
        vertice_antecessor = fila[0]
        print("Fila:", fila)
        for aresta in vertices[vertice_antecessor].get_arestas():
            if aresta[0] not in visitados:
                visitados.append(aresta[0])
                historico.append([aresta[0], vertice_antecessor])
                fila.append(aresta[0])
        
        fila.pop(0)
    
    print()
    print(visitados)
    print(historico)

    # pilha = [inicio]
    # visitados = [inicio]
    # # antecessores = [-1]
    # # distancia_percorrida = 0
    # # distancia_caminho = -1
    # caminho = []
    # while pilha:
    #     vertice_antecessor = pilha[-1]
    #     print("Pilha:", pilha)
    #     for aresta in vertices[vertice_antecessor].get_arestas():
    #         if aresta[0] not in visitados:
    #             pilha.append(aresta[0])
    #             # distancia_percorrida += aresta[1]
    #             if aresta[0] == fim:
    #                 print("Caminho: ", pilha)
    #                 print("Novo caminho\n")
    #                 caminho = pilha.copy()
    #                 pilha = []
    #             else:
    #                 visitados.append(aresta[0])
            
    #             break

    #         if aresta == vertices[vertice_antecessor].arestas[-1]:
    #             # distancia_percorrida -= aresta[1]
    #             pilha.pop()


    # caminho = []
    # if not caminho:
    #     print(f"Não possui caminho de {inicio} até {fim}. :(")
    # else:
    #     caminho.reverse()
    #     print("Tem caminho!")
    #     print(caminho)

    caminho = []
    if fim not in visitados:
        print(f"Não possui caminho de {inicio} até {fim}. :(")
    else:
        print("Tem caminho!")
        vertice = fim
        while vertice != inicio:
            caminho.append(vertice)
            vertice = historico[visitados.index(vertice)][1]

        caminho.append(vertice)
        print(caminho)

    print()
    return caminho
        