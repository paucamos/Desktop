import numpy as np


def process_element(vecinos):
    #[valor, vecinos]
    valor = vecinos[0]  # Valor original
    valores = vecinos[1]  # Vecinos sin valor original

    valores.append(valor)

    return round(sum(valores) / len(valores), 2)


def process_matrix(matriz):

    neighbors = []
    new_matrix = np.zeros(shape=(len(matriz), len(matriz)))

    for i in range(len(matriz)):
        for j, value in enumerate(matriz[i]):

            if i == 0 or i == len(matriz) - 1 or j == 0 or j == len(matriz[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0:
                    new_neighbors.append(matriz[i - 1][j])  # top neighbor
                if j != len(matriz[i]) - 1:
                    new_neighbors.append(matriz[i][j + 1])  # right neighbor
                if i != len(matriz) - 1:
                    new_neighbors.append(matriz[i + 1][j])  # bottom neighbor
                if j != 0:
                    new_neighbors.append(matriz[i][j - 1])  # left neighbor

            else:
                # add neighbors
                new_neighbors = [
                    matriz[i - 1][j],  # top neighbor
                    matriz[i][j + 1],  # right neighbor
                    matriz[i + 1][j],  # bottom neighbor
                    matriz[i][j - 1]   # left neighbor
                ]

            neighbors.append({
                "value": value,
                "neighbors": new_neighbors})

            new_matrix[i][j] = process_element([value, new_neighbors])

    # return neighbors
    return [matriz, neighbors, new_matrix]


if __name__ == '__main__':
    print(process_matrix(np.random.randint(1, 100, size=(5, 5))))
