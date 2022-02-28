def fibo_generator_even():
    """
    Генератор Фибоначчи за время O(n)
    yield: четное число Фибоначчи
    """
    n_1 = 0
    n_2 = 1
    while True:
        if n_1 % 2 == 0:
            yield n_1
        n_1, n_2 = n_2, n_1 + n_2


def fibo_list(n):
    out = list()
    fibo = fibo_generator_even()
    for i in range(n):
        out.append(next(fibo))
    return out


if __name__ == "__main__":
    print(fibo_list(4))
