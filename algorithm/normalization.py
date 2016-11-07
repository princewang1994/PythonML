import numpy as np

def z_score(data):
    return (data - data.mean(0)) / data.std()