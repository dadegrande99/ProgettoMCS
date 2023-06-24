import math
import numpy as np


def custom_dct(image):
    dim = len(image)
    dct_image = np.zeros(dim)

    for k in range(dim):
        dct_image[k] = np.sqrt(2/dim) * np.sum(image * np.cos((np.pi/dim) * k * (np.arange(dim) + 0.5)))

        if k == 0:
            dct_image[k] *= 1/np.sqrt(2)
    return dct_image

def custom_dct2(matrix):
    #avremo in input un'immagine che dovremo convertire in un numpy array
    rows, cols = matrix.shape
    dct_matrix = np.zeros_like(matrix, dtype=float)

    for i in range(rows):
        for j in range(cols):
            sum = 0.0
            coeff_u = 1 if i == 0 else np.sqrt(2)
            coeff_v = 1 if j == 0 else np.sqrt(2)
            for u in range(rows):
                for v in range(cols):
                    pixel_value = matrix[u, v]
                    cosine_u = np.cos((2 * u + 1) * i * np.pi / (2*rows))
                    cosine_v = np.cos((2 * v + 1) * j * np.pi / (2*cols))
                    sum += pixel_value * cosine_u * cosine_v
            dct_matrix[i, j] = sum * coeff_u * coeff_v / np.sqrt(rows*cols)
    return dct_matrix