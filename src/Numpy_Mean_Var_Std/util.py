import numpy as np


def calculate_statistics(array: list[list[int]]):
    arr = np.array(array)

    mean = np.mean(arr, axis=1)
    variance = np.var(arr, axis=0)
    standard_deviation = round(float(np.std(arr)), 11)

    return mean, variance, standard_deviation
