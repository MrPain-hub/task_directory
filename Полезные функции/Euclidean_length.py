from functools import reduce


def length(a, b):
    L = max(len(a), len(b))
    X = []
    for i in range(L):
        X += [(a[i] - b[i])**2]
    return (reduce(lambda x1, x2: x1 + x2, X))**1/2


def locate_point_L2(a, r, x2='all'):
    x1, y1 = a
    if x2 == 'all':
        x2 = [i for i in range(x1 - r, x1 + r + 1)]
        for xi in x2:
            k1 = (r ** 2 - (xi - x1) ** 2) ** (1 / 2) + y1
            k2 = -(r ** 2 - (xi - x1) ** 2) ** (1 / 2) + y1
            yield [xi, k1]
            if k1 != k2:
                yield [xi, k2]
    else:
        k1 = (r**2 - (x2 - x1)**2)**(1/2) + y1
        k2 = -(r**2 - (x2 - x1)**2)**(1/2) + y1
        yield [x2, k1]
        if k1 != k2:
            yield [x2, k2]


if __name__ == '__main__':
    #a = list(map(float, input().split()))
    #b = list(map(float, input().split()))
    a = [-129.103, -234.254]
    b = [-79.095,-234.254]
    print(f"длина = {length(a, b)}")

    a = (1, 1)
    r = 3
else:
    print(f"Import file {__name__}")