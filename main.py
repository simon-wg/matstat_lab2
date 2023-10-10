import numpy as np


def main():
    """ Main program """
    ex_matrix = np.matrix([[0, 1 / 3, 1 / 3, 1 / 3], [0, 0, 1 / 2, 1 / 2], [1, 0, 0, 0], [1 / 2, 0, 1 / 2, 0]])
    lmbda = float(input("What is lambda?: "))
    print(taskA(ex_matrix, lmbda))


def taskA(matrix, lmbda):
    adj_matrix = chain_to_adjacency(matrix)
    return q_ify(taskB(adj_matrix, lmbda))


def taskB(adj_matrix, lmbda):
    for index, row in enumerate(adj_matrix):
        row *= (1 - lmbda) / row.sum()
        row += lmbda / row.size
    return adj_matrix


def q_ify(a):
    return np.linalg.matrix_power(a, 100)[0, :]


def chain_to_adjacency(matrix):
    n_values = []
    for row in matrix.tolist():
        count = 0
        for element in row:
            if element > 0:
                count += 1
        n_values.append(count)
    adj_matrix = []
    for index, row in enumerate(matrix):
        row = row.tolist()[0]
        adj_matrix.append(np.array(row) * n_values[index])
    return np.matrix(adj_matrix)

main()
