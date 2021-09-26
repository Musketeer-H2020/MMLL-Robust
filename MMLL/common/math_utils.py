import numpy as np


def cosine_similarity(a, b):
    a = np.squeeze(a)
    b = np.squeeze(b)
    assert a.shape[0] == b.shape[0]
    return np.sum(a * b) / (np.linalg.norm(a) * np.linalg.norm(b))
