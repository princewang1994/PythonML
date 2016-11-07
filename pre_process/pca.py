import scipy as sp
import numpy as np
from algorithm import normalization as norm

def pca(data, k):
    mat = norm.z_score(data)
    cov = sp.cov(mat.T)
    x, y = np.linalg.eig(cov)
    ind = np.argsort(-x)
    ft = y[:, ind[:k]]
    return np.dot(mat, ft), ft