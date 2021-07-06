def busca_profundidade(grafo, inicio, fim):
    print("BUSCA EM PROFUNDIDADE")

    vertices = grafo.get_vertices()

    pilha = [inicio, inicio]
    visitados = [inicio]
    antecessores = [-1]
    while pilha:
        vertice_antecessor = pilha.pop()
        for aresta in vertices[vertice_antecessor].get_arestas():
            if aresta[0] not in visitados:
                visitados.append(aresta[0])
                antecessores.append(vertice_antecessor)
                pilha.append(aresta[0])
                pilha.append(aresta[0])
                break
        
        # print("Pilha:", pilha)
    
    print()
    # print(visitados)
    # print(antecessores)

    caminho = []
    if fim not in visitados:
        print(f"Não possui caminho de {inicio} até {fim}. :(")
    else:
        print("Tem caminho!")
        vertice = fim
        while vertice != inicio:
            caminho.append(vertice)
            vertice = antecessores[visitados.index(vertice)]

        caminho.append(vertice)
        print(caminho)

    print()
    return caminho
        