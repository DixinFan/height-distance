def z_score_normalize(data, dim):
    mean, std = 0, 0
    if dim == 'x':
        mean = 0.4903
        std = 0.135
    if dim == 'y':
        mean = 120
        std = 40.32
    data = (data - mean) / std
    return data


def poly(x, y):
    p00 = 170.5
    p10 = -15.12
    p01 = -0.09411
    p20 = -0.3339
    p11 = -5.108
    p02 = 0.2122
    p21 = -0.07972
    p12 = -0.4506
    p03 = 0.7971
    height = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
    return height

