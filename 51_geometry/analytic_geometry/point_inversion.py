"""
    Context:
        p = (pᵢ, pⱼ)

"""


def invert_point(pi, pj, qx, qy):
    return [2 * qx - pi, 2 * qy - pj]


"""
References:
    https://en.wikipedia.org/wiki/Point_reflection
"""
