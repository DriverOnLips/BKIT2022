from math import sqrt


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(-(root ** 0.5))
        result.append((root ** 0.5))
    elif D > 0.0:
        sqD = sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.append(-(root1 ** 0.5))
            result.append((root1 ** 0.5))
        if root2 > 0:
            result.append(-(root2 ** 0.5))
            result.append((root2 ** 0.5))
    return result
