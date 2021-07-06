def busca_largura(grafo, inicio, fim):
    print("BUSCA EM LARGURA")

    vertices = grafo.get_vertices()

    fila = [inicio]
    visitados = [inicio]
    antecessores = [-1]
    while fila:
        vertice_antecessor = fila[0]
        for aresta in vertices[vertice_antecessor].get_arestas():
            if aresta[0] not in visitados:
                visitados.append(aresta[0])
                antecessores.append(vertice_antecessor)
                fila.append(aresta[0])
        
        # print("Fila:", fila)
        fila.pop(0)
    
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
        