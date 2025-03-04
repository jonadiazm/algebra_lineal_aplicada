import matplotlib.pyplot as plt
import numpy as np


def plot_vectors(vecs, cols, alpha=1):

    plt.axvline(x=0, color="grey", zorder=0)
    plt.axhline(y=0, color="grey", zorder=0)

    for i in range(len(vecs)):
        x = np.concatenate([[0, 0], vecs[i]])
        plt.quiver(
            [x[0]],
            [x[1]],
            [x[2]],
            [x[3]],
            angles="xy",
            scale_units="xy",
            scale=1,
            color=cols[i],
            alpha=alpha,
        )

def plot_matrix(matrix, vector_col=["red", "blue"], alpha=1):
    
    # unitary circle
    x = np.linspace(-1, 1, 100000)
    y = np.sqrt(1 - x**2)

    # transformed circle
    x1 = matrix[0,0]*x + matrix[0,1]*y
    y1 = matrix[1,0]*x + matrix[1,1]*y
    x1_neg = matrix[0,0]*x - matrix[0,1]*y
    y1_neg = matrix[1,0]*x - matrix[1,1]*y

    # vectors
    u1 = matrix[:, 0]
    v1 = matrix[:, 1]

    plot_vectors([u1, v1], cols=[vector_col[0], vector_col[1]], alpha=alpha)

    plt.plot(x1, y1, color="green", alpha = 0.7)
    plt.plot(x1_neg, y1_neg, color="green", alpha = 0.7)

    plt.gca().set_aspect('equal')