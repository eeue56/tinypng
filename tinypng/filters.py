
def paeth_predictor(a, b, c):
    p = (a + b) - c

    distances = [p - a,
        p - b,
        p - c]

    points = [a, b, c]

    return points[distances.index(min(distances))]
