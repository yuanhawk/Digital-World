import numpy as np


def normalize_minmax(data):
    shape = list(data.shape)

    if len(shape) == 1:
        return None
    elif shape[1] >= 1:
        for i in range(shape[1]):
            high = np.max(data[:, i])
            low = np.min(data[:, i])

            data[:, i] = (data[:, i] - low) / (high - low)
            return data