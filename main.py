from matplotlib import pyplot as plt
from graph_knn import Graph_knn
from busca_largura import busca_largura
from busca_profundidade import busca_profundidade

def pega_inicio_fim(limite_inferior, limite_superior):
    """Recebe valores de início e fim e os resotna no formato [inicio, fim]."""
    inicio = int(input(f"Digite o vértice inicial, entre {limite_inferior} e {limite_superior}: "))
    fim = int(input(f"Digite o vértice final, entre {limite_inferior} e {limite_superior}, excluindo o {inicio}: "))
    print()
    print(f"O vértice {inicio} é o inicio e o vértice {fim} é o fim.")
    print()

    return [inicio, fim]


def plotar_grafo(grafo, caminho=[], ordenacao="Ordenação não especificada"):
    """Plota grafo."""
    xs = []
    ys = []
    xs_caminho = []
    ys_caminho = []
    vertices = grafo.get_vertices()
    v = grafo.v
    k = grafo.k

    print("Aguarde enquanto configuramos a ferramenta gráfica.")

    for index in caminho:
            xs_caminho.append(vertices[index].get_x())
            ys_caminho.append(vertices[index].get_y())

    for i in range(0, len(vertices)):
        if i not in caminho:
            xs.append(vertices[i].get_x())
            ys.append(vertices[i].get_y())
    
    plt.plot(xs, ys, '.')

    if caminho:
        plt.plot(xs_caminho, ys_caminho, color='red')
        plt.plot(xs_caminho.pop(0), ys_caminho.pop(0), "*", color='red')
        plt.plot(xs_caminho, ys_caminho, "o", color='orange')


    plt.axis([0-v*0.05, v*1.05, 0-v*0.05, v*1.05])
    plt.title(f'{ordenacao} - Grafo knn com {v} vertices e k = {k} - O caminho encontrado tem {len(caminho)} vértices') 
    print("Em instantes o grafo será plotado...")
    plt.show()
    print("Ferramenta gráfica encerrada.")
    print()


def main():
    print('Grafo KNN')

    v = 10000
    k = 5

    grafo_knn = Graph_knn(v, k)

    [inicio, fim] = pega_inicio_fim(0, v-1)

    caminho = busca_largura(grafo_knn, inicio, fim)
    plotar_grafo(grafo_knn, caminho, "Busca em largura")

    caminho = busca_profundidade(grafo_knn, inicio, fim)
    plotar_grafo(grafo_knn, caminho, "Busca em profundidade")


if(__name__ == "__main__"):
    main()